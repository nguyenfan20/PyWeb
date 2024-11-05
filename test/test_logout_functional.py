#TEST ĐĂNG XUẤT
from driver import *
from selenium.webdriver.common.by import By
import time

def test_logout_funtional(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Log Out')]").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//a[contains(text(), 'Log In')]").text
    time.sleep(1)
    assert "Log In" in result

