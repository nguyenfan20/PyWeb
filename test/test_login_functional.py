#TEST ĐĂNG NHẬP
from driver import *
from selenium.webdriver.common.by import By
import time

#Test đăng nhập với thông tin hợp lệ
def test_valid_login_functional(driver):
    valid_account(driver)
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//a[contains(text(), 'Nguyen Phan')]").text
    time.sleep(1)
    assert "Nguyen Phan" in result

#Test đăng nhập khi trường mật khẩu trống
def test_empty_pwd(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Log In')]").click()
    driver.find_element(By.ID, "usrname").send_keys("nguyenfan")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Login')]").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Incorrect Username or Password" in result

#Test đăng nhập khi trường tên người dùng trống
def test_empty_username(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Log In')]").click()
    driver.find_element(By.ID, "usrname").send_keys("")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Login')]").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Incorrect Username or Password" in result

#Test đăng nhập khi nhập sai mật khẩu
def test_invalid_password(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Log In')]").click()
    driver.find_element(By.ID, "usrname").send_keys("nguyenfan")
    driver.find_element(By.ID, "password").send_keys("12345")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Login')]").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//div[@class='alert alert-danger']").text
    assert "Incorrect Username or Password" in result