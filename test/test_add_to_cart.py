#TEST THÊM VÀO GIỎ HÀNG
from driver import *
from selenium.webdriver.common.by import By
import time

#Test thêm 1 sản phẩm vào giỏ hàng
def test_add_to_cart(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[1]/div/div/a").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "cartCounter").text
    time.sleep(1)
    assert "1" in result
