#TEST GỬI FORM
from .driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Test gửi biểu mẫu
def test_form_submission(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Contact')]").click()
    driver.find_element(By.ID, "career-name").send_keys("Nguyen")
    position = Select(driver.find_element(By.ID, "career-position"))
    position.select_by_visible_text("BackEnd Enginer")
    time.sleep(2)
    file_input = driver.find_element(By.ID, "career-resume")
    file_input.send_keys("C:/Users/nguye/Downloads/image/words.jpg")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/button").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Đã gửi liên lạc tới admin" 