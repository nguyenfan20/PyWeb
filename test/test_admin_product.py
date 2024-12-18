import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .driver import *


def validate_price_and_amount(price, amount):
    # Kiểm tra giá sản phẩm
    if not re.match(r"^\d+(\.\d{1,2})?$", price) or float(price) < 0:
        return False, f"Giá sản phẩm '{price}' không hợp lệ. Giá phải là số dương và có thể có tối đa 2 chữ số thập phân."
    
    # Kiểm tra số lượng sản phẩm
    if not amount.isdigit() or int(amount) < 0:
        return False, f"Số lượng sản phẩm '{amount}' không hợp lệ. Số lượng phải là số nguyên dương."
    
    # Nếu cả hai điều kiện đều hợp lệ
    return True, "Giá và số lượng hợp lệ."

def test_add_product_admin(driver):
    # Đăng nhập vào tài khoản hợp lệ
    valid_account(driver)

    # Truy cập trang quản lý sản phẩm
    driver.get("http://127.0.0.1:5000/admin/product/")

    # Chờ và tìm nút 'Create New Record' rồi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Create New Record']"))
    ).click()

    # Dữ liệu sản phẩm cần thêm
    input_data = {
        "name": "Laptop con cá",
        "price": "200",
        "image": "static\\images\\product\\Acer\\acer06.jpg",
        "amount": "20",
        "brand": "Acer"
    }

    # Nhập dữ liệu vào form
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-group input#name"))
    )
    name_input.clear()
    name_input.send_keys(input_data["name"])
    time.sleep(1)

    price_input = driver.find_element(By.CSS_SELECTOR, "input#price")
    price_input.clear()
    price_input.send_keys(input_data["price"])
    time.sleep(1)

    image_input = driver.find_element(By.CSS_SELECTOR, "#image")
    image_input.clear()
    image_input.send_keys(input_data["image"])
    time.sleep(1)

    amount_input = driver.find_element(By.CSS_SELECTOR, "#amount")
    amount_input.clear()
    amount_input.send_keys(input_data["amount"])
    time.sleep(1)

    select_element = driver.find_element(By.CSS_SELECTOR, "#brand")
    select_element.click()
    option = driver.find_element(By.CSS_SELECTOR, "#brand option[value='4']")  # Acer
    option.click()
    time.sleep(1)

    # Bấm nút 'Save' để lưu sản phẩm
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Save']"))
    )
    save_button.click()

    # Quay lại trang danh sách sản phẩm
    driver.get("http://127.0.0.1:5000/admin/product/")

    # Chờ cho các dòng trong bảng xuất hiện
    rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table tbody tr"))
    )

    # Lấy dòng đầu tiên trong bảng
    first_row = rows[0]
    cells = first_row.find_elements(By.CSS_SELECTOR, "td")
    assert len(cells) >= 13, "Dữ liệu trong bảng không đủ cột."
    
    brand_cell = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td.col-brand")
    # Lấy dữ liệu sản phẩm từ bảng
    product_data = {
        "name": cells[3].text.strip(),
        "price": cells[4].text.strip(),
        "image": cells[5].text.strip(),
        "amount": cells[6].text.strip(),
        "brand": brand_cell.text.strip()
    }

    # In dữ liệu lấy được để kiểm tra
    print(f"Dữ liệu sản phẩm: {product_data}")
    print(f"Giá trị thương hiệu (brand): '{product_data['brand']}'")
    assert product_data["name"] == input_data["name"], "Tên sản phẩm không khớp."
    assert float(product_data["price"]) == float(input_data["price"]), "Giá sản phẩm không khớp."
    assert product_data["image"] == input_data["image"], "Hình ảnh sản phẩm không khớp."
    assert product_data["amount"] == input_data["amount"], "Số lượng sản phẩm không khớp."
    assert product_data["brand"] == input_data["brand"], "Thương hiệu sản phẩm không khớp."

    print("Sản phẩm đã được thêm thành công và thông tin khớp với dữ liệu đầu vào.")

def test_add_product_empty_name(driver):
    # Đăng nhập vào tài khoản hợp lệ
    valid_account(driver)

    # Truy cập trang quản lý sản phẩm
    driver.get("http://127.0.0.1:5000/admin/product/")

    # Chờ và tìm nút 'Create New Record' rồi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Create New Record']"))
    ).click()

    # Để trống trường tên sản phẩm và điền các thông tin khác
    input_data = {
        "name": "",
        "price": "200",
        "image": "static\\images\\product\\Acer\\acer06.jpg",
        "amount": "20",
        "brand": "4"
    }

    # Tìm trường tên sản phẩm và nhập dữ liệu
    name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-group input#name"))
        )
    name_input.clear()
    name_input.send_keys(input_data["name"])  # Tên sản phẩm để trống

    # Điền các thông tin khác
    price_input = driver.find_element(By.CSS_SELECTOR, "input#price")
    price_input.clear()
    price_input.send_keys(input_data["price"])

    image_input = driver.find_element(By.CSS_SELECTOR, "#image")
    image_input.clear()
    image_input.send_keys(input_data["image"])

    amount_input = driver.find_element(By.CSS_SELECTOR, "#amount")
    amount_input.clear()
    amount_input.send_keys(input_data["amount"])

    select_element = driver.find_element(By.CSS_SELECTOR, "#brand")
    select_element.click()

    option = driver.find_element(By.CSS_SELECTOR, "#brand option[value='4']")
    option.click()
    time.sleep(2)

    # Kiểm tra nếu tên sản phẩm trống trước khi bấm "Save"
    if input_data["name"] == "":
        assert False, "Bạn chưa nhập tên sản phẩm. Save button should be disabled when product name is empty."
    else:
        # Nếu tên không rỗng, bấm nút Save
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Save']"))
        )
        save_button.click()

def test_add_product_invalid_infor(driver):
    # Đăng nhập vào tài khoản hợp lệ
    valid_account(driver)

    # Truy cập trang quản lý sản phẩm
    driver.get("http://127.0.0.1:5000/admin/product/")

    # Chờ và tìm nút 'Create New Record' rồi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Create New Record']"))
    ).click()

    # Để trống trường tên sản phẩm và điền các thông tin khác
    input_data = {
        "name": "Laptop con cá",
        "price": "-200",
        "image": "static\\images\\product\\Acer\\acer06.jpg",
        "amount": "abc",
        "brand": "4"
    }

    # Tìm trường tên sản phẩm và nhập dữ liệu
    name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-group input#name"))
        )
    name_input.clear()
    name_input.send_keys(input_data["name"])  # Tên sản phẩm để trống

    # Điền các thông tin khác
    price_input = driver.find_element(By.CSS_SELECTOR, "input#price")
    price_input.clear()
    price_input.send_keys(input_data["price"])

    image_input = driver.find_element(By.CSS_SELECTOR, "#image")
    image_input.clear()
    image_input.send_keys(input_data["image"])

    amount_input = driver.find_element(By.CSS_SELECTOR, "#amount")
    amount_input.clear()
    amount_input.send_keys(input_data["amount"])

    select_element = driver.find_element(By.CSS_SELECTOR, "#brand")
    select_element.click()

    option = driver.find_element(By.CSS_SELECTOR, "#brand option[value='4']")
    option.click()
    time.sleep(2)

    # Gọi hàm kiểm tra giá và số lượng
    is_valid, message = validate_price_and_amount(input_data["price"], input_data["amount"])

    # Nếu không hợp lệ, hiển thị thông báo lỗi
    if not is_valid:
        assert False, message
    else:
        # Nếu hợp lệ, tiếp tục bấm nút Save
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Save']"))
        )
        save_button.click()
        
def test_edit_product_by_id(driver):
    # Đăng nhập và truy cập trang quản lý sản phẩm
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/admin/product/")
    
    # Đợi trang tải xong và tìm tất cả các dòng sản phẩm trong bảng
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table tbody tr")))
    
    # Lấy tất cả các dòng trong bảng sản phẩm
    rows = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")
    
    # Chọn sản phẩm đầu tiên trong bảng
    first_row = rows[0]
    cells = first_row.find_elements(By.CSS_SELECTOR, "td")
    
    assert len(cells) >= 1, "Không có sản phẩm nào trong danh sách để chỉnh sửa."
    
    # Giả sử ID sản phẩm nằm ở cột đầu tiên
    product_id = cells[0].text.strip()
    time.sleep(2)
    
    # Tìm thẻ chỉnh sửa cho sản phẩm này
    edit_button = first_row.find_element(By.XPATH, ".//a[@title='Edit Record']")
    edit_button.click()  # Click vào chỉnh sửa
    
    # Chờ sự xuất hiện của phần tử trường tên sản phẩm
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#name")))
    
    # Chỉnh sửa tên sản phẩm thành 'Laptop con mèo'
    name_input = driver.find_element(By.CSS_SELECTOR, "input#name")
    original_name = name_input.get_attribute("value")  # Lấy tên sản phẩm hiện tại
    time.sleep(2)
    
    # Nếu tên hiện tại không phải 'Laptop con mèo', thì thay đổi nó
    if original_name != "Laptop con mèo":
        name_input.clear()  # Xóa dữ liệu cũ
        name_input.send_keys("Laptop con mèo")  # Nhập tên mới
        save_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Save']")
        save_button.click()  # Lưu thay đổi
        print("Đã thay đổi tên sản phẩm thành 'Laptop con mèo'")
    else:
        print("Tên sản phẩm đã là 'Laptop con mèo', không cần thay đổi.")
        driver.get("http://127.0.0.1:5000/admin/product/")
    
    # Đợi trang quay lại danh sách sản phẩm
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table tbody tr")))
    
    # Kiểm tra tên sản phẩm trong bảng sau khi quay lại
    rows = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")
    first_row = rows[0]
    cells = first_row.find_elements(By.CSS_SELECTOR, "td")
    
    assert len(cells) >= 4, "Bảng sản phẩm không đủ cột để kiểm tra tên sản phẩm."
    
    product_name = cells[3].text.strip()  # Giả sử tên sản phẩm ở cột thứ 4
    assert product_name == "Laptop con mèo", f"Tên sản phẩm không thay đổi. Hiện tại: {product_name}"
    
    print("Tên sản phẩm đã được thay đổi thành công.")                                          

def test_delete_product_by_id(driver):
    # Đăng nhập và truy cập trang quản lý sản phẩm
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/admin/product/")

    # Đợi trang tải xong và tìm tất cả các dòng sản phẩm trong bảng
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table tbody tr")))

    # Lấy tất cả các dòng trong bảng sản phẩm
    rows = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")

    # Chọn sản phẩm đầu tiên trong bảng
    first_row = rows[0]
    cells = first_row.find_elements(By.CSS_SELECTOR, "td")

    if len(cells) >= 1:
        # Tìm thẻ form xóa cho sản phẩm này
        delete_form = first_row.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/form/button")

        # Đảm bảo form và nút xóa đã được tải đầy đủ
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(delete_form))

        # Tìm nút xóa và nhấp vào
        delete_button = delete_form.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/form/button")
        delete_button.click()

        # Kiểm tra xem hộp thoại xác nhận có hiển thị đúng không
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())  # Đợi hộp thoại xuất hiện
        assert alert.text == "Are you sure you want to delete this record?", f"Thông báo xác nhận không đúng, nhận được: {alert.text}"

        # Chấp nhận hộp thoại xác nhận xóa
        alert.accept()  # Nhấn "OK" để xác nhận

        # Kiểm tra xem sản phẩm đã bị xóa chưa bằng cách đợi và kiểm tra bảng sản phẩm
        WebDriverWait(driver, 10).until(EC.staleness_of(first_row))

        # Kiểm tra sản phẩm đã biến mất
        rows_after_delete = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")
        assert len(rows_after_delete) < len(rows)  # Đảm bảo số lượng sản phẩm giảm đi
