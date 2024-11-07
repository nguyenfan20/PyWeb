#TEST CÁC CHỨC NĂNG CỦA GIỎ HÀNG
from driver import *
from selenium.webdriver.common.by import By
import time

#Test giỏ hàng có cập nhật sau khi thêm nhiều sản phẩm
def test_update_cart(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//img[@alt='Metronic Shop UI']").click()
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[1]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[2]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[3]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    time.sleep(2)
    quantity = driver.find_element(By.ID, "cart_quantity").text
    time.sleep(2)
    assert "3" in quantity

#Test xóa sản phẩm trong cart
def test_delete_product(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//img[@alt='Metronic Shop UI']").click()
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[1]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[2]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[3]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "del-goods").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    driver.refresh()
    time.sleep(2)
    quantity = driver.find_element(By.ID, "cart_quantity").text
    time.sleep(2)
    assert "2" in quantity

#Test continue shopping button in cart
def test_continue_button(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[1]/div/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//button[@class='btn btn-default']").click()
    time.sleep(2)
    assert "http://127.0.0.1:5000/product-list" in driver.current_url
