#TEST TÌM KIẾM
from driver import *
from selenium.webdriver.common.by import By
import time

#Test chức năng tìm kiếm
def test_search_functional(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("Laptop")
    driver.find_element(By.XPATH, f"//button[@type='submit']").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//em[contains(text(), 'Laptop')]").text
    assert "Laptop" in result

#Test tìm kiếm với không nhập gì cả
def test_empty_search(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("")
    driver.find_element(By.XPATH, f"//button[@type='submit']").click()
    time.sleep(2)
    assert "http://127.0.0.1:5000/product-list?kw=" in driver.current_url

#Test tìm kiếm với các ký tự đặc biệt
def test_invalid_search(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("!?/#$%")
    driver.find_element(By.XPATH, f"//button[@type='submit']").click()
    time.sleep(2)
    result = driver.find_element(By.XPATH, f"//img[@alt='']").get_attribute("src")
    assert "/static/images/no-product.jpg" in result


