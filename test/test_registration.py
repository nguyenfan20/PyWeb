#TEST ĐĂNG KÝ
from driver import *
from selenium.webdriver.common.by import By
import time

#Test chức năng đăng ký khi điền đầy đủ thông tin
def test_registration(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User1")
    driver.find_element(By.ID, "username").send_keys("standard2012") #Nhớ thay đổi username và email mỗi khi chạy để tránh bị lỗi
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    driver.find_element(By.ID, "email").send_keys("example123@example123.vn")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(2)
    assert "http://127.0.0.1:5000/user-login" in driver.current_url

#Test đăng ký với trường fullname trống (với bất kỳ trường nào trống cũng được)
def test_empty_fullname_registration(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    fullname_field = driver.find_element(By.ID, "fullname")
    fullname_field.send_keys("")
    driver.find_element(By.ID, "username").send_keys("standard12346")
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    driver.find_element(By.ID, "email").send_keys("example123@example1.vn")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(5)
    validation_mess = fullname_field.get_attribute("validationMessage")
    assert validation_mess == "Please fill out this field.", "Thông báo không xuất hiện"

#Test đăng ký với username đã tồn tại
def test_exist_username_registration(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User")
    driver.find_element(By.ID, "username").send_keys("standard2012")
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    driver.find_element(By.ID, "email").send_keys("example123@example.vn")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(2)
    alert_mess = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Check your information again/Username might already exit" in alert_mess

#Test đăng ký với mật khẩu không khớp
def test_not_match_pwd_registration(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User")
    driver.find_element(By.ID, "username").send_keys("standard123467")
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    driver.find_element(By.ID, "email").send_keys("example123@example.vn")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123457")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(2)
    alert_mess = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Password not match" in alert_mess

#Test đăng ký với nút Reset
def test_reset_button(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User")
    driver.find_element(By.ID, "username").send_keys("standard123467")
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    driver.find_element(By.ID, "email").send_keys("example123@example.vn")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[@type='reset']").click()
    time.sleep(2)

    assert driver.find_element(By.ID, "fullname").get_attribute("value") == ""
    assert driver.find_element(By.ID, "username").get_attribute("value") == ""
    assert driver.find_element(By.ID, "phone").get_attribute("value") == ""
    assert driver.find_element(By.ID, "email").get_attribute("value") == ""
    assert driver.find_element(By.ID, "password").get_attribute("value") == ""
    assert driver.find_element(By.ID, "confirm-password").get_attribute("value") == ""