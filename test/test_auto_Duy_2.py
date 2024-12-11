#TEST ĐĂNG NHẬP
from .driver import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_forgot_password(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, "//a[@href='/user-login']").click()
    driver.find_element(By.XPATH, "//a[@href='/user-forget-password']").click()

    driver.find_element(By.ID, "email").send_keys("quangduy.phung03@gmail.com")
    time.sleep(5)

    button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Send']")
    button.click()
    time.sleep(5)
    
    try:
         WebDriverWait(driver, 5).until(
            EC.alert_is_present()  # Wait until the alert box is present
        )
         alert = driver.switch_to.alert
         alert_text = alert.text
         print(f"Alert message: {alert_text}")
         assert "OTP has been sent!" in alert_text, f"Expected message not found. Found: {alert_text}"
         
    except Exception as e:
        # Print error and page source for debugging
        print("Test failed: OTP was not sent. Unable to reset password.")
        print(f"Error: {e}")
        print(driver.page_source)  # Log the page source
        assert False, "Test failed: OTP was not sent."

