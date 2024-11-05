import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#Hàm tự động nhập username và password
def valid_account (driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Log In')]").click()
    driver.find_element(By.ID, "usrname").send_keys("nguyenfan")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Login')]").click()