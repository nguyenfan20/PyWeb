import pytest
from app.utils import cart_stats

def test_cart_stats_empty_cart():
    # Test với giỏ hàng rỗng
    cart = {}
    result = cart_stats(cart)
    
    assert result == {
        "total_quantity": 0,
        "total_amount": 0
    }, "Hàm không xử lý đúng giỏ hàng rỗng"

def test_cart_stats_single_product():
    # Test với một sản phẩm
    cart = {
        '1': {
            'quantity': 2,
            'product_price': 100
        }
    }
    result = cart_stats(cart)
    
    assert result == {
        "total_quantity": 2,
        "total_amount": 200
    }, "Hàm không tính toán đúng cho một sản phẩm"

def test_cart_stats_multiple_products():
    # Test với nhiều sản phẩm
    cart = {
        '1': {
            'quantity': 2,
            'product_price': 100
        },
        '2': {
            'quantity': 3,
            'product_price': 50
        }
    }
    result = cart_stats(cart)
    
    assert result == {
        "total_quantity": 5,
        "total_amount": 350
    }, "Hàm không tính toán đúng cho nhiều sản phẩm"

def test_cart_stats_zero_quantity():
    # Test với sản phẩm có số lượng 0
    cart = {
        '1': {
            'quantity': 0,
            'product_price': 100
        }
    }
    result = cart_stats(cart)
    
    assert result == {
        "total_quantity": 0,
        "total_amount": 0
    }, "Hàm không xử lý đúng sản phẩm có số lượng 0"

def test_cart_stats_none_input():
    # Test với input là None
    cart = None
    result = cart_stats(cart)
    
    assert result == {
        "total_quantity": 0,
        "total_amount": 0
    }, "Hàm không xử lý đúng khi input là None"