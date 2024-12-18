import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .driver import *


def test_add_user(driver):
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/admin/users/")

    # Chờ và tìm nút 'Create New Record' rồi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@title='Create New Record']"))
    ).click()

    input_data = {
        "active": "1",
        "name": "Bui Truong Thinh",
        "user_name": "bokho",
        "password": "123",
        "phone": "0337992538",
        "email": "thinhbui230903@gmail.com",
        "role": "ADMIN"
    }
    time.sleep(1)

    input_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-group input#active"))
    )
    input_active.clear()
    input_active.send_keys(input_data["active"])
    time.sleep(1)

    input_name = driver.find_element(By.CSS_SELECTOR, "input#name")
    input_name.clear()
    input_name.send_keys(input_data["name"])
    time.sleep(1)

    input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
    input_username.clear()
    input_username.send_keys(input_data["user_name"])
    time.sleep(1)

    input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
    input_password.clear()
    input_password.send_keys(input_data["password"])
    time.sleep(1)

    input_phone = driver.find_element(By.CSS_SELECTOR, "input#phone")
    input_phone.clear()
    input_phone.send_keys(input_data["phone"])
    time.sleep(1)

    input_email = driver.find_element(By.CSS_SELECTOR, "input#email")
    input_email.clear()
    input_email.send_keys(input_data["email"])
    time.sleep(1)

    select_role = driver.find_element(By.CSS_SELECTOR, "#role")
    select_role.click()
    time.sleep(1)
    select = driver.find_element(
        By.CSS_SELECTOR, "#role option[value='ADMIN']")  # admin
    select.click()
    time.sleep(1)

    # Bấm nút 'Save' để lưu sản phẩm
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Save']"))
    )
    save_button.click()

    driver.get("http://127.0.0.1:5000/admin/users/")

        # Chờ bảng dữ liệu tải xong
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody"))
    )
    # Lấy thẻ <tr> đầu tiên trong bảng
    first_row = driver.find_element(By.CSS_SELECTOR, "table tbody tr")

    # Kiểm tra giá trị trong các thẻ <td> của dòng đầu tiên
    cols = first_row.find_elements(By.CSS_SELECTOR, "td")

    # So sánh các giá trị với dữ liệu đã nhập
    assert cols[2].text == input_data["name"], f"Expected name: {input_data['name']}, but got: {cols[2].text}"
    assert cols[3].text == input_data["user_name"], f"Expected username: {input_data['user_name']}, but got: {cols[3].text}"
    assert cols[4].text == input_data["phone"], f"Expected phone: {input_data['phone']}, but got: {cols[4].text}"
    assert cols[5].text == input_data["email"], f"Expected email: {input_data['email']}, but got: {cols[5].text}"

    print("Dữ liệu trong bảng khớp với dữ liệu đã nhập.")

def test_add_user_empty_name(driver):
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/admin/users/")

    # Chờ và tìm nút 'Create New Record' rồi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@title='Create New Record']"))
    ).click()

    input_data = {
        "active": "",
        "name": "",
        "user_name": "bokho",
        "password": "123",
        "phone": "0337992538",
        "email": "thinhbui230903@gmail.com",
        "role": "ADMIN"
    }
    time.sleep(1)

    input_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-group input#active"))
    )
    input_active.clear()
    input_active.send_keys(input_data["active"])
    time.sleep(1)

    input_name = driver.find_element(By.CSS_SELECTOR, "input#name")
    input_name.clear()
    input_name.send_keys(input_data["name"])
    time.sleep(1)

    input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
    input_username.clear()
    input_username.send_keys(input_data["user_name"])
    time.sleep(1)

    input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
    input_password.clear()
    input_password.send_keys(input_data["password"])
    time.sleep(1)

    input_phone = driver.find_element(By.CSS_SELECTOR, "input#phone")
    input_phone.clear()
    input_phone.send_keys(input_data["phone"])
    time.sleep(1)

    input_email = driver.find_element(By.CSS_SELECTOR, "input#email")
    input_email.clear()
    input_email.send_keys(input_data["email"])
    time.sleep(1)

    select_role = driver.find_element(By.CSS_SELECTOR, "#role")
    select_role.click()
    time.sleep(1)
    select = driver.find_element(
        By.CSS_SELECTOR, "#role option[value='ADMIN']")  # admin
    select.click()
    time.sleep(1)

    # Bấm nút 'Save' để lưu sản phẩm
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Save']"))
    )
    save_button.click()

    if input_name.get_attribute("value") == "" or input_active.get_attribute("value") == "":
        validation_mess = input_name.get_attribute("validationMessage")
        assert validation_mess == "Vui lòng điền vào trường này." 
    else:
        driver.get("http://127.0.0.1:5000/admin/users/")
        print(f"Thêm thành công")

def test_add_user_invalid_phone(driver):
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/admin/users/")

    # Chờ và tìm nút 'Create New Record' rồi click
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@title='Create New Record']"))
    ).click()

    input_data = {
        "active": "1",
        "name": "Bui Truong Thinh",
        "user_name": "bokho",
        "password": "123",
        "phone": "abcd1234",  # Nhập chữ vào trường phone
        "email": "thinhbui230903@gmail.com",
        "role": "ADMIN"
    }
    time.sleep(1)

    # Điền các trường thông tin khác
    input_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-group input#active"))
    )
    input_active.clear()
    input_active.send_keys(input_data["active"])
    time.sleep(1)

    input_name = driver.find_element(By.CSS_SELECTOR, "input#name")
    input_name.clear()
    input_name.send_keys(input_data["name"])
    time.sleep(1)

    input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
    input_username.clear()
    input_username.send_keys(input_data["user_name"])
    time.sleep(1)

    input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
    input_password.clear()
    input_password.send_keys(input_data["password"])
    time.sleep(1)

    # Nhập chữ vào trường phone
    input_phone = driver.find_element(By.CSS_SELECTOR, "input#phone")
    input_phone.clear()
    input_phone.send_keys(input_data["phone"])
    time.sleep(1)

    input_email = driver.find_element(By.CSS_SELECTOR, "input#email")
    input_email.clear()
    input_email.send_keys(input_data["email"])
    time.sleep(1)

    select_role = driver.find_element(By.CSS_SELECTOR, "#role")
    select_role.click()
    time.sleep(1)
    select = driver.find_element(
        By.CSS_SELECTOR, "#role option[value='ADMIN']")  # admin
    select.click()
    time.sleep(1)

    # Bấm nút 'Save' để lưu sản phẩm
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Save']"))
    )
    save_button.click()

     # Kiểm tra nếu số điện thoại có chữ
    if any(char.isalpha() for char in input_data["phone"]):
        # Nếu có chữ, xác nhận và in thông báo lỗi
        assert False, "Số điện thoại không hợp lệ." 
        
    else:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody"))
        )
        # Lấy thẻ <tr> đầu tiên trong bảng
        first_row = driver.find_element(By.CSS_SELECTOR, "table tbody tr")

        # Kiểm tra giá trị trong các thẻ <td> của dòng đầu tiên
        cols = first_row.find_elements(By.CSS_SELECTOR, "td")

        # So sánh các giá trị với dữ liệu đã nhập
        assert cols[2].text == input_data["name"], f"Expected name: {input_data['name']}, but got: {cols[2].text}"
        assert cols[3].text == input_data["user_name"], f"Expected username: {input_data['user_name']}, but got: {cols[3].text}"
        assert cols[4].text == input_data["phone"], f"Expected phone: {input_data['phone']}, but got: {cols[4].text}"
        assert cols[5].text == input_data["email"], f"Expected email: {input_data['email']}, but got: {cols[5].text}"
        print(f"Thêm thành công")

def test_delete_user(driver):
    # Đăng nhập và truy cập trang quản lý sản phẩm
    valid_account(driver)
    driver.get("http://127.0.0.1:5000/admin/users/")

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
        time.sleep()
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

    print(f"Xoá thành công")