from .driver import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random 


def test_cancel_order(driver):
    valid_account(driver)
    wait = WebDriverWait(driver, 2)
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/user-edit-account']").click()
    time.sleep(1)
    
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/orders']").click()

    driver.find_element((By.XPATH, "//button[@class='btn-action' and text()='Cancel']")).click()
    time.sleep(1)

    confirm_box = driver.switch_to.alert

    # Lấy nội dung văn bản của hộp thoại confirm
    confirm_text = confirm_box.text
    print(f"Nội dung của hộp thoại confirm: {confirm_text}")

    confirm_box.accept()  # Nhấn "OK"
    time.sleep(2)
    
    confirm_box2 = driver.switch_to.alert

    # Lấy nội dung văn bản của hộp thoại confirm
    confirm_text = confirm_box2.text
    print(f"Nội dung của hộp thoại confirm: {confirm_text}")

    confirm_box2.accept()  # Nhấn "OK"
    time.sleep(2)
    try:
        wait.until(EC.url_to_be("http://localhost:5000/orders"))
        # If the URL is correct, the test passes
    except TimeoutException:
        # If not redirected to the cart page, fail the test
        assert False, "Failed to redirect to the cart page after reorder."
   
   
    
def test_reorder(driver):
    valid_account(driver)
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/user-edit-account']").click()
    time.sleep(1)
    
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/orders']")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@class='btn-action' and text()='Reorder']").click()
    time.sleep(1)

    # Handle the confirmation dialog
    alert = Alert(driver)
    alert.accept()  # Simulate clicking "OK"
    time.sleep(3)
    
    try:
        assert "http://localhost:5000/cart" in driver.current_url
        # If the URL is correct, the test passes
    except TimeoutException:
        # If not redirected to the cart page, fail the test
        assert False, "Failed to redirect to the cart page after reorder."
    
    
    
def test_upd_empty_profile_fullname(driver):
    valid_account(driver)
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/user-edit-account']").click()
    time.sleep(1)

    fullname_field = driver.find_element(By.ID, "fullname")
    fullname_field.clear()  # Clear existing text

    driver.find_element(By.XPATH, "//button[@type='submit' and text()='Continue']").click()
    time.sleep(2)

    try:
    # Tìm thông báo với nội dung "Failed updated"
        failed_alert = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger")
        assert "Failed updated" in failed_alert.text, "Expected 'Failed updated' message not found."
    # Kiểm tra URL có đúng không
        assert "http://localhost:5000/user-edit-account" in driver.current_url

    except TimeoutException:
    # Ném lỗi nếu không tìm thấy thông báo hoặc URL không đúng
        assert False, "Failed to update: TimeoutException occurred."

    
    
def test_review_product(driver):
    valid_account(driver)
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//a[@href='/product-list']").click()
    time.sleep(3)

    # Danh sách các XPATH của các sản phẩm
    products_xpath = [
        "//a[@href='/item-detail?product-id=1']",
        "//a[@href='/item-detail?product-id=2']",
        "//a[@href='/item-detail?product-id=7']",
        "//a[@href='/item-detail?product-id=8']",
        "//a[@href='/item-detail?product-id=9']",
        "//a[@href='/item-detail?product-id=3']"
    ]

# Chọn ngẫu nhiên một sản phẩm
    selected_product_xpath = random.choice(products_xpath)
    time.sleep(2)
    driver.find_element(By.XPATH, selected_product_xpath).click()
    time.sleep(5)
    # Tìm phần tử Reviews và nhấn vào nó
    driver.find_element(By.XPATH, "//a[@href='#Reviews' and @data-toggle='tab']").click()
    time.sleep(2)  
    
    driver.find_element(By.ID, "name").send_keys("Ngọc Huyền")
    time.sleep(1)  
    
    driver.find_element(By.ID, "email").send_keys("huyen@gmail.com")
    time.sleep(2)  
    
    driver.find_element(By.ID, "review").send_keys("sản phẩm tốt, bền")
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//button[@type='submit' and text()='Send']").click()
    time.sleep(2)

# Kiểm tra xem nội dung của trang có chứa thông báo lỗi không
    page_source = driver.page_source

# Nếu có thông báo lỗi "Internal Server Error", test case sẽ thất bại
    if "Internal Server Error" in page_source:
      pytest.fail("Test failed. Internal Server Error encountered.")
    else:
    # Nếu không có thông báo lỗi, in ra thông báo pass
      print("Test passed. No internal server error.") 
    
      
def test_icon_facebook_link(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, "//a[contains(@class, 'facebook')]").click()
    
    try:
        current_url = driver.current_url

    # Kiểm tra URL phải là trang Facebook của cửa hàng
        expected_facebook_url = "https://www.facebook.com/LaptopUTE"
        assert expected_facebook_url in current_url, f"Expected URL '{expected_facebook_url}', but got '{current_url}'."
    except:
        assert False, "Failed to navigate to Facebook page: Timeout occurred."
    
    
    
def is_url_invalid(driver):
    current_url = driver.current_url
    page_source = driver.page_source

    # Kiểm tra xem URL có phải là trang lỗi không (404 hoặc Not Found)
    if "404" in current_url or "Not Found" in page_source or "The requested URL was not found on the server" in page_source:
        return True
    return False

# Kiểm tra điều hướng vào các trang
def test_store_information(driver):
    driver.get("http://localhost:5000/")

    # Các liên kết cần điều hướng
    links = [
        ("Delivery Information", "/delivery-info"),
        ("Customer Service", "/customer-service"),
        ("Order Tracking", "/order-tracking"),
        ("Shipping & Returns", "/shipping-returns"),
        ("Contact Us", "/contact-us"),
        ("Careers", "/careers"),
        ("Payment Methods", "/payment-methods")
    ]
    
    previous_url = ""  # Để lưu URL trước đó và so sánh
    errors = []  # Danh sách lưu các lỗi gặp phải trong test case

    # Kiểm tra điều hướng đến các trang mong muốn
    for link_text, expected_url in links:
        try:
            # Tìm liên kết và nhấp vào
            driver.find_element(By.LINK_TEXT, link_text).click()
            time.sleep(2)  # Thời gian chờ để trang tải

            # Kiểm tra URL và trạng thái trang
            if is_url_invalid(driver) or driver.current_url == previous_url:
                error_message = f"Test case failed: {link_text} - URL is invalid or page not found!"
                errors.append(error_message)
                print(error_message)

            # Kiểm tra xem URL có phải là trang mong muốn không
            expected_full_url = f"http://localhost:5000{expected_url}"
            if driver.current_url != expected_full_url:
                error_message = f"Test case failed: {link_text} - Expected URL: {expected_full_url}, but got {driver.current_url}"
                errors.append(error_message)
                print(error_message)

            # In ra URL của trang hiện tại sau khi nhấn
            print(f"Đã điều hướng đến trang: {driver.current_url}")
            
            # Cập nhật previous_url để so sánh với lần sau
            previous_url = driver.current_url

            # Quay lại trang chủ để thử tiếp liên kết khác
            driver.back()
            time.sleep(2)  # Thời gian chờ để trang trở lại

        except Exception as e:
            error_message = f"Lỗi khi nhấp vào liên kết {link_text}: {e}"
            errors.append(error_message)
            print(error_message)

    # Sau khi kiểm tra tất cả các liên kết, kiểm tra xem có lỗi không
    if errors:
        print("Các lỗi phát hiện trong quá trình kiểm thử:")
        for error in errors:
            print(error)
        assert False, "Có lỗi trong các chức năng điều hướng!"

    else:
        print("Tất cả các chức năng điều hướng đều hoạt động bình thường.")
       
        
def test_twitter_link_contact(driver):
    driver.get("http://localhost:5000/")
    try:
    # Tìm phần tử Twitter timeline
        twitter_link = driver.find_element(By.CSS_SELECTOR, "a.twitter-timeline")
    
    # Lấy URL mong đợi từ thuộc tính href
        expected_url = twitter_link.get_attribute("href")
    
    # Click vào đường link
        twitter_link.click()
    
    # Chờ điều hướng sang trang mới
        time.sleep(3)
    
    # Lấy URL hiện tại sau khi điều hướng
        current_url = driver.current_url
    
    # Kiểm tra URL hiện tại có khớp với URL mong đợi
        assert current_url != "http://localhost:5000/", "Test failed: Still on the homepage."
        assert "twitter.com" in current_url, f"Test failed: Did not navigate to Twitter. Current URL: {current_url}"
        
        print("Test passed: Successfully navigated to Twitter.")

    except TimeoutException:
        assert False, "Test failed: Timeout occurred while waiting for navigation to Twitter."

    except Exception as e:
        assert False, f"Test failed with error: {str(e)}"
        
        
def test_buying_without_select_paying_method(driver):
    valid_account(driver)
    driver.find_element(By.XPATH, "//a[@href='/product-list']").click()
    time.sleep(3)

    # Danh sách các XPATH của các sản phẩm
    products_xpath = [
        "//a[@href='/item-detail?product-id=1']",
        "//a[@href='/item-detail?product-id=2']",
        "//a[@href='/item-detail?product-id=7']",
        "//a[@href='/item-detail?product-id=8']",
        "//a[@href='/item-detail?product-id=9']",
        "//a[@href='/item-detail?product-id=3']"
    ]

# Chọn ngẫu nhiên một sản phẩm
    selected_product_xpath = random.choice(products_xpath)
    time.sleep(2)
    driver.find_element(By.XPATH, selected_product_xpath).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(@class, 'btn btn-primary add2cart') and contains(@onclick, 'addToCart(')]").click()
    time.sleep(1)

    # Mở giỏ hàng
    driver.find_element(By.CSS_SELECTOR, ".fa.fa-shopping-cart").click()
    time.sleep(1)
    
  # Sau khi thêm sản phẩm vào giỏ hàng, thực hiện thanh toán
    driver.find_element(By.XPATH, "//button[@type='button' and text()='Checkout ']").click()  

    # Bước 1: CHOOSE YOUR CITY
    driver.find_element(By.XPATH, "//a[contains(@href, '#shipping-address-content')]").click()
   # Chọn dropdown thành phố
    city_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "mySelect"))  # Sử dụng ID đúng cho dropdown thành phố
)

# Sử dụng Select để lấy tất cả các tùy chọn từ dropdown
    select = Select(city_dropdown)
    all_options = select.options

# Lọc các tùy chọn (bỏ "--Please Select--" ra ngoài)
    valid_options = [option for option in all_options if option.text != '--Please Select--']
# Chọn một thành phố ngẫu nhiên từ danh sách các tùy chọn hợp lệ
    random_city = random.choice(valid_options)
    random_city.click()

    # Bước 3: CONFIRM ORDER
    step3_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#confirm-content')]"))
    )
    step3_link.click()

# Nhấn vào nút xác nhận đơn hàng
    confirm_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "button-confirm"))
)
    confirm_button.click()
    time.sleep(2)

    try:
        # Tìm thông báo lỗi
        alert_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Please select paying method')]")
        
        # Nếu tìm thấy thông báo, test pass
        print("Test passed: 'Please select paying method' message displayed.")
        
    except:
        # Nếu không tìm thấy thông báo, test fail
        assert False, "Test failed: 'Please select paying method' message not displayed."

def test_change_pw(driver):
    valid_account(driver)
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/user-edit-account']").click()
    time.sleep(1)
    
    driver.find_element(By.CSS_SELECTOR, "li > a[href='/user-change-password']").click()
    time.sleep(1)  
    
    driver.find_element(By.ID, "old-password").send_keys("12345")
    driver.find_element(By.ID, "new-password").send_keys("123")
    driver.find_element(By.ID, "confirm-password").send_keys("123")
    driver.find_element(By.XPATH, "//button[@type='submit' and text()='Change']").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "usrname").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.XPATH, "//button[@type='submit' and text()='Login']").click()
    
    try:
        wait.until(EC.url_to_be("http://127.0.0.1:5000/"))
    except TimeoutException:
        assert False, "Failed to change password"
    