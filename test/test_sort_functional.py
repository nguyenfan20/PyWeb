#TEST SẮP XẾP
from .driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Test sắp xếp từ bé > lớn
def test_low_to_high_sort(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Products')]").click()
    combobox_sort = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@class='form-control input-sm']"))
    )
    select = Select(combobox_sort)
    select.select_by_value("/product-list?sort=lowtohigh")
    time.sleep(2)
    assert driver.current_url == "http://127.0.0.1:5000/product-list?sort=lowtohigh", "URL không khớp"

#Test sắp xếp từ lớn > bé
def test_high_to_low_sort(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Products')]").click()
    combobox_sort = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@class='form-control input-sm']"))
    )
    select = Select(combobox_sort)
    select.select_by_value("/product-list?sort=hightolow")
    time.sleep(2)
    assert driver.current_url == "http://127.0.0.1:5000/product-list?sort=hightolow", "URL không khớp"