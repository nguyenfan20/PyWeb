import pytest
from unittest.mock import patch, MagicMock
from app.utils import get_totalprice 


# Test Case 1: Kiểm tra với uid không có hóa đơn
@patch('app.utils.get_receiptsbyuid', return_value=[])
@patch('app.utils.get_receiptdetail', return_value=[])
def test_no_receipts(mock_receiptsbyuid, mock_receiptdetail):
    uid = 1
    result = get_totalprice(uid)
    assert result == {}, "Expected an empty dictionary when there are no receipts."


# Test Case 2: Kiểm tra với uid có hóa đơn, không có chi tiết hóa đơn
@patch('app.utils.get_receiptsbyuid', return_value=[MagicMock(id=1)])
@patch('app.utils.get_receiptdetail', return_value=[])
def test_receipts_no_details(mock_receiptsbyuid, mock_receiptdetail):
    uid = 2
    result = get_totalprice(uid)
    assert result == {1: 0}, "Expected a dictionary with receipt ID 1 and value 0."


# Test Case 3: Kiểm tra với uid có nhiều hóa đơn, có chi tiết hóa đơn
@patch('app.utils.get_receiptsbyuid')
@patch('app.utils.get_receiptdetail')
def test_multiple_receipts_with_details(mock_receiptsbyuid, mock_receiptdetail):
    # Mock giá trị trả về từ get_receiptsbyuid
    mock_receipt1 = MagicMock(id=1)  # Giả lập đối tượng Receipt với thuộc tính id
    mock_receipt2 = MagicMock(id=2)  # Giả lập đối tượng Receipt với thuộc tính id
    mock_receiptsbyuid.return_value = [mock_receipt1, mock_receipt2]

    # Mock giá trị trả về từ get_receiptdetail
    mock_detail1 = MagicMock(receipt_id=91, quantity=2, unit_price=50)
    mock_detail2 = MagicMock(receipt_id=92, quantity=3, unit_price=30)
    mock_detail3 = MagicMock(receipt_id=91, quantity=1, unit_price=20)
    mock_receiptdetail.return_value = [mock_detail1, mock_detail2, mock_detail3]

    # Kiểm tra kết quả
    uid = 3
    result = get_totalprice(uid)

    # Kiểm tra kết quả trả về có đúng không
    # Kết quả mong đợi {1: 140, 2: 90}, vì tổng giá trị của hóa đơn với id 1 là 140 và id 2 là 90
    assert result == {1: 140, 2: 90}


# Test Case 4: Kiểm tra chi tiết hóa đơn không khớp với hóa đơn
@patch('app.utils.get_receiptsbyuid', return_value=[MagicMock(id=1)])
@patch('app.utils.get_receiptdetail', return_value=[
    {'receitp_id': 2, 'quantity': 2, 'unit_price': 50},
])
def test_details_do_not_match(mock_receiptsbyuid, mock_receiptdetail):
    uid = 4
    result = get_totalprice(uid)
    assert result == {1: 0}, "Expected a dictionary with receipt ID 1 and value 0."


# Test Case 5: Kiểm tra với hóa đơn và chi tiết bị trùng
@patch('app.utils.get_receiptsbyuid', return_value=[{'id': 1}])
@patch('app.utils.get_receiptdetail', return_value=[
    {'receitp_id': 1, 'quantity': 2, 'unit_price': 50},
    {'receitp_id': 1, 'quantity': 2, 'unit_price': 50},
])
def test_duplicate_details(mock_receiptsbyuid, mock_receiptdetail):
    uid = 5
    result = get_totalprice(uid)
    assert result == {1: 200}, "Expected total price to account for duplicate details."


# Test Case 6: Kiểm tra khi các hàm trả về None
@patch('app.utils.get_receiptsbyuid', return_value=None)
@patch('app.utils.get_receiptdetail', return_value=None)
def test_none_returns(mock_receiptsbyuid, mock_receiptdetail):
    uid = 6
    with pytest.raises(TypeError):
        get_totalprice(uid)
