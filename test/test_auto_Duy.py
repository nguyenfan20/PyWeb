#TEST ĐĂNG KÝ
from .driver import *
from selenium.webdriver.common.by import By
import time


#Test đăng ký khi không nhập @ vào email
def test_regex_registration(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User1")
    driver.find_element(By.ID, "username").send_keys("standard2003") #Nhớ thay đổi username và email mỗi khi chạy để tránh bị lỗi
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("example.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(2)
    validation_mess = email_field.get_attribute("validationMessage")
    assert validation_mess == "Please include an '@' in the email address. 'example.com' is missing an '@'."

#Test đăng ký nhập sai email
def test_wrong_email(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User1")
    driver.find_element(By.ID, "username").send_keys("standard2003") #Nhớ thay đổi username và email mỗi khi chạy để tránh bị lỗi
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("example@.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(2)
    validation_mess = email_field.get_attribute("validationMessage")
    assert validation_mess == "'.' is used at a wrong position in '.com'."

#Test đăng ký nhập chữ vào số điện thoại
def test_enter_text_into_phonebox(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User1")
    driver.find_element(By.ID, "username").send_keys("standard16")
    phone_field = driver.find_element(By.ID, "phone")
    phone_field.send_keys("abc")
    driver.find_element(By.ID, "email").send_keys("example123@example1.vn")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "confirm-password").send_keys("123456")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    time.sleep(5)
    validation_mess = phone_field.get_attribute("validationMessage")
    assert validation_mess == "Please fill out this field."

#Test đăng ký nhập mật khẩu ngắn hơn 5 chữ số 
def test_short_password_registration(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Registration')]").click()
    driver.find_element(By.ID, "fullname").send_keys("Standard User1")
    driver.find_element(By.ID, "username").send_keys("standard16")
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    driver.find_element(By.ID, "email").send_keys("example123@example1.vn")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "confirm-password").send_keys("1234")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Create an account')]").click()
    alert_mess = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Password is shorter than 5 character" in alert_mess