import pytest
from flask import Flask
from app.utils import edit_infor 
from app.models import Users, db
from werkzeug.security import generate_password_hash

@pytest.fixture(scope='session')
def app():
    app = Flask(__name__)
    
    # Cấu hình test database
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Khởi tạo db với app
    db.init_app(app)
    
    # Tạo context
    with app.app_context():
        db.create_all()
    
    yield app
    
    # Cleanup
    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='function')
def app_context(app):
    with app.app_context():
        yield
        db.session.rollback()

@pytest.fixture
def create_test_user(app):
    def _create_user(**kwargs):
        # Thêm giá trị mặc định nếu không được cung cấp
        defaults = {
            'active': True,
            'password': generate_password_hash("defaultpassword"),
            # Thêm các giá trị mặc định khác nếu cần
        }
        defaults.update(kwargs)
        
        user = Users(**defaults)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        return user
    
    return _create_user

def test_edit_infor_success(app_context, create_test_user):
    # Tạo user để test
    test_user = create_test_user(
        username="test_user", 
        name="Old Name", 
        email="old_email@example.com", 
        phone="123456789"
    )
    
    # Test cập nhật thành công
    result = edit_infor("test_user", "New Name", "new_email@example.com", "987654321")
    
    assert result is True, "Hàm không trả về True khi cập nhật thành công"
    
    # Kiểm tra user đã được cập nhật
    updated_user = Users.query.filter_by(username="test_user").first()
    assert updated_user.name == "New Name", "Tên không được cập nhật chính xác"
    assert updated_user.email == "new_email@example.com", "Email không được cập nhật chính xác"
    assert updated_user.phone == "987654321", "Số điện thoại không được cập nhật chính xác"

def test_edit_infor_user_not_found(app_context):
    # Test không tìm thấy user
    result = edit_infor("nonexistent_user", "New Name", "new_email@example.com", "987654321")
    
    assert result is False, "Hàm không trả về False khi user không tồn tại"

def test_edit_infor_commit_fail(app_context, create_test_user, monkeypatch):
    # Tạo user để test
    test_user = create_test_user(
        username="commit_test_user", 
        name="Old Name", 
        email="old_email@example.com", 
        phone="123456789"
    )

    # Mock commit để gây lỗi
    def mock_commit():
        raise Exception("Commit failed")
    
    monkeypatch.setattr(db.session, 'commit', mock_commit)

    # Test commit thất bại
    result = edit_infor("commit_test_user", "New Name", "new_email@example.com", "987654321")
    
    assert result is False, "Hàm không trả về False khi commit thất bại"