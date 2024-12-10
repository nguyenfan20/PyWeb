import pytest
import os
from app import app, db
from app.models import Product
from app.utils import get_product
from sqlalchemy.orm import scoped_session


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/tmdt?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_SIZE = 2


@pytest.fixture(scope="session")
def test_client():
    # Lưu lại cấu hình cũ
    old_config = {
        'SQLALCHEMY_DATABASE_URI': app.config['SQLALCHEMY_DATABASE_URI'],
        'TESTING': app.config.get('TESTING', False),
        'PAGE_SIZE': app.config.get('PAGE_SIZE', 12)
    }

    # Áp dụng cấu hình test
    app.config.update(
        SQLALCHEMY_DATABASE_URI=TestConfig.SQLALCHEMY_DATABASE_URI,
        TESTING=TestConfig.TESTING,
        PAGE_SIZE=TestConfig.PAGE_SIZE
    )

    # Tạo client test
    with app.test_client() as client:
        with app.app_context():
            yield client

    # Khôi phục cấu hình cũ
    app.config.update(old_config)


@pytest.fixture(scope="function")
def test_session(test_client):
    connection = db.engine.connect()
    transaction = connection.begin()  # Bắt đầu transaction

    # Tạo session mới cho mỗi test
    options = dict(bind=connection, binds={})
    session = scoped_session(db.sessionmaker(**options))

    # Tạo dữ liệu test
    test_products = [
        Product(id=113, name="Laptop Dell XPS", price=1000, brand_id=1),
        Product(id=114, name="Laptop HP Pavilion", price=800, brand_id=2),
        Product(id=115, name="Laptop Dell Inspiron", price=600, brand_id=1),
        Product(id=116, name="Laptop Lenovo ThinkPad", price=1200, brand_id=3)
    ]

    for product in test_products:
        session.merge(product)
        session.commit()
  # Commit dữ liệu test vào transaction

    yield session

    # Rollback sau mỗi test
    transaction.rollback()  # Hoàn tác tất cả thay đổi trong transaction
    connection.close()      # Đóng kết nối
    session.remove()        # Loại bỏ session


def test_get_all_products(test_session):
    try:
        products = get_product()
        assert len(products) == 46, f"Expected 4 products, but got {len(products)}"
    except AssertionError as e:
        print(f"Test failed: {e}")
        raise  # Ném lại lỗi để pytest ghi nhận bài kiểm thử thất bại
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise  # Ném lại lỗi nếu có lỗi không mong đợi



def test_search_by_keyword(test_session):
    products = get_product(kw="Dell")
    assert len(products) == 9
    assert all("Dell" in p.name for p in products)


def test_filter_by_brand(test_session):
    products = get_product(brand_id=1)
    assert len(products) == 10
    assert all(p.brand_id == 1 for p in products)


def test_sorting(test_session):
    products = get_product(sort="lowtohigh")
    prices = [p.price for p in products]
    assert prices == sorted(prices)


def test_pagination(test_session):
    page1_products = get_product(page=1)
    assert len(page1_products) == 2


def test_combined_filters(test_session):
    products = get_product(
        kw="Dell",
        brand_id=1,
        sort="lowtohigh",
        page=1
    )
    assert len(products) <= app.config["PAGE_SIZE"]
    assert all("Dell" in p.name for p in products)
    assert all(p.brand_id == 1 for p in products)
    prices = [p.price for p in products]
    assert prices == sorted(prices)


def test_invalid_inputs(test_session):
    products = get_product(page=0)
    assert len(products) == 46


def test_edge_cases(test_session):
    products = get_product(page=9999)
    assert len(products) == 0

def test_advanced_filters(test_session):
    products = get_product(
        kw="Laptop",  
        brand_id=3,   
        sort="hightolow",  
        page=1        
    )
    assert len(products) <= app.config["PAGE_SIZE"], f"Expected products <= {app.config['PAGE_SIZE']}, but got {len(products)}"
    assert all("Laptop" in p.name for p in products), "Expected all products to contain 'Laptop' in their name"
    assert all(p.brand_id == 3 for p in products), "Expected all products to have brand_id = 3"
    prices = [p.price for p in products]
    assert prices == sorted(prices, reverse=True), "Expected prices to be sorted in descending order"
