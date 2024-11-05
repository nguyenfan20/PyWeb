#TEST GỬI FORM
from driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Test gửi biểu mẫu
def test_form_submission(driver):
    form_url = "http://127.0.0.1:5000/careers"
    success_url = "http://127.0.0.1:5000/careers?"
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Contact')]").click()
    driver.find_element(By.ID, "career-name").send_keys("Nguyen")
    position = Select(driver.find_element(By.ID, "career-position"))
       #Danh sách các vị trí
    # options = ["FrontEnd Modifier", "BackEnd Enginer", "Technical Support Engineer"]
    # for option in options:
    #     position.select_by_visible_text(option)
    #     selected_position = position.first_selected_option.text
    #     assert selected_position == option, f"Expected {option}, but got {selected_position}"
    #     print(f"Successfully selected: {selected_position}")
    position.select_by_visible_text("BackEnd Enginer")
    file_input = driver.find_element(By.ID, "career-resume")
    file_input.send_keys("C:/Users/nguye/Downloads/image/words.jpg")
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/button").click()
    time.sleep(1)
    current_url = driver.current_url
    assert current_url == success_url, f"Expected URL to be {success_url}, but got {current_url}"
