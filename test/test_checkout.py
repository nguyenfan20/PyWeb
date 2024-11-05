#TEST THANH TOÁN
from driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_checkout(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
    driver.find_element(By.CLASS_NAME, "form-control").send_keys("Laptop")
    driver.find_element(By.XPATH, f"//button[@type='submit']").click()
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div/div[2]/div[3]/div[1]/div/a").click()
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    driver.find_element(By.XPATH, f"//button[@type = 'button']").click()
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 1: Choose your city')]").click()
    time.sleep(2)
    city = Select(driver.find_element(By.ID, "mySelect"))
    city.select_by_visible_text("Hà Nội")
    time.sleep(2)
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 2: Payment Method')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='radio' and @name='paymentmethod']").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//button[@class='btn btn-primary pull-right']").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    alert2 = driver.switch_to.alert
    alert2.accept()
    time.sleep(2)
    result = driver.find_element(By.ID, "cartCounter").text
    assert "0" in result
