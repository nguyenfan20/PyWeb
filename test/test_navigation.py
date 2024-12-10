#TEST ĐIỀU HƯỚNG
from .driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Test trang chủ
def test_homepage_navigation(driver):
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)
    assert "Laptop UTE" in driver.title

#Test trang sản phẩm
def test_product_navigation(driver):
    driver.get("http://127.0.0.1:5000/product-list")
    time.sleep(2)
    assert "Laptop UTE's Product" in driver.title #Expected Product

#Test cụ thể trang chi tiết sản phẩm 
def test_detail_product_navigation(driver):
    driver.get("http://127.0.0.1:5000/item-detail?product-id=27")
    time.sleep(2)
    assert "Laptop UTE's Detail Product" in driver.title

#Test trang liên hệ
def test_contact_navigation(driver):
    driver.get("http://127.0.0.1:5000/careers")
    time.sleep(2)
    assert "Laptop UTE's Contact" in driver.title

#Test trang admin
def test_admin_navigation(driver):
    driver.get("http://127.0.0.1:5000/admin/")
    time.sleep(2)
    assert "Laptop UTE's ADMIN" in driver.title