# TEST THANH TOÁN
from driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from test_add_to_cart import test_add_multiple_products_to_cart
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# def test_checkout(driver):
#     valid_account(driver)
#     driver.find_element(By.XPATH, f"//i[@class='fa fa-search search-btn']").click()
#     driver.find_element(By.CLASS_NAME, "form-control").send_keys("Laptop")
#     driver.find_element(By.XPATH, f"//button[@type='submit']").click()
#     driver.find_element(By.XPATH, f"/html/body/div[4]/div/div/div[2]/div[3]/div[1]/div/a").click()
#     driver.find_element(By.XPATH, f"//i[@class='fa fa-shopping-cart']").click()

#     driver.find_element(By.XPATH, f"//button[@type = 'button']").click()
#     driver.find_element(By.XPATH, f"//a[contains(text(),'Step 1: Choose your city')]").click()
#     time.sleep(2)
#     city = Select(driver.find_element(By.ID, "mySelect"))
#     city.select_by_visible_text("Hà Nội")
#     time.sleep(2)
#     driver.find_element(By.XPATH, f"//a[contains(text(),'Step 2: Payment Method')]").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@type='radio' and @name='paymentmethod']").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "button-payment-method").click()


#     time.sleep(2)
#     driver.find_element(By.XPATH, f"//button[@class='btn btn-primary pull-right']").click()
#     time.sleep(2)
#     alert = driver.switch_to.alert
#     alert.accept()
#     time.sleep(2)
#     alert2 = driver.switch_to.alert
#     alert2.accept()
#     time.sleep(2)
#     result = driver.find_element(By.ID, "cartCounter").text
#     assert "0" in result

def test_checkout_with_multiple_products(driver):
    # Gọi lại hàm thêm 5 sản phẩm vào giỏ hàng
    test_add_multiple_products_to_cart(driver)
    #click vào nút checkout 
    driver.find_element(By.XPATH, f"//button[@type = 'button']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 1: Choose your city')]").click()
    time.sleep(2)
    city = Select(driver.find_element(By.ID, "mySelect"))
    selected_city = "Hà Nội"
    city.select_by_visible_text(selected_city)
    time.sleep(2)
    driver.find_element(By.XPATH, f"//a[contains(text(),'Step 2: Payment Method')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='radio' and @name='paymentmethod']").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(3)
    try:
        # Chờ thẻ span có giá trị
        checkout_quantity_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div/div[3]/div[2]/div/div/div[2]/ul/li[1]/strong/span[@id='cart_quantity']"))
        )
        checkout_quantity = int(checkout_quantity_element.text.strip())
        
        # Tìm thẻ tbody chứa danh sách sản phẩm
        tbody_element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[3]/div[2]/div/div/div[1]/table/tbody")
        # Lấy danh sách tất cả các thẻ <tr> trong tbody
        product_rows = tbody_element.find_elements(By.TAG_NAME, "tr")
        print(f"Lấy được các thẻ tr")
    except Exception as e:
        print(f"Lỗi khi tìm thẻ tr: {e}")
    
    # Khởi tạo tổng số lượng sản phẩm
    total_quantity = 0

    # Lặp qua từng hàng (trừ hàng đầu tiên chứa tiêu đề)
    for row in product_rows:
        # Lấy tất cả các thẻ <td> trong hàng
        cells = row.find_elements(By.TAG_NAME, "td")

        # Kiểm tra xem hàng này có chứa dữ liệu sản phẩm không
        if len(cells) > 0:
            try:
                # Tìm thẻ input trong div.product-quantity
                input_element = cells[2].find_element(By.XPATH, ".//div[@class='product-quantity']/input[@type='number']")
                # Lấy giá trị của thuộc tính value
                quantity_value = int(input_element.get_attribute("value").strip())
                # Cộng vào tổng số lượng
                total_quantity += quantity_value
            except Exception as e:
                print(f"Lỗi khi lấy giá trị số lượng sản phẩm: {e}")

    # So sánh tổng số lượng sản phẩm với giá trị trong <span id="cart_quantity">
    if checkout_quantity == total_quantity:
        print("Tổng số lượng sản phẩm trong checkout KHỚP với tổng sản phẩm của hóa đơn.")
    else:
        print(f"Tổng số lượng sản phẩm trong checkout KHÔNG KHỚP. Tổng sản phẩm của hóa đơn là: {checkout_quantity}, tổng số lượng: {total_quantity}")

    # Kiểm tra thành phố trong giỏ hàng
    try:
        # Lấy giá trị thành phố từ thẻ <span id="selectedValue">
        selected_value_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div/div[3]/div[2]/div/div/div[2]/ul/li[2]/strong/span[@id='selectedValue']"))
        )
        selected_value = selected_value_element.text.strip()
        print(f"Thành phố hiển thị trong giỏ hàng: {selected_value}")
        
        # So sánh thành phố đã chọn và thành phố hiển thị
        if selected_city == selected_value:
            print("Thành phố trong checkout KHỚP với thành phố đã chọn.")
        else:
            print(f"Thành phố trong checkout KHÔNG KHỚP. Thành phố đã chọn: {selected_city}, thành phố hiển thị: {selected_value}")

    except Exception as e:
        print(f"Lỗi khi kiểm tra thành phố: {e}")

    # Lấy giá trị tổng tiền từ thẻ <span id="cart_amount">
    try:
        cart_amount_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div/div[3]/div[2]/div/div/div[2]/ul/li[3]/strong/span[@id='cart_amount']"))
        )
        cart_amount = float(cart_amount_element.text.strip().replace(',', '').replace('$', ''))  # Loại bỏ định dạng nếu có
        print(f"Tổng tiền hiển thị trong checkout: {cart_amount}")
    except Exception as e:
        print(f"Lỗi khi lấy giá trị tổng tiền: {e}")

    try:
        # Lấy tất cả các thẻ <tr> chứa sản phẩm trong tbody
        tbody_element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[3]/div[2]/div/div/div[1]/table/tbody")
        product_rows = tbody_element.find_elements(By.TAG_NAME, "tr")
        
        # Khởi tạo biến tổng tiền
        total_amount = 0.0

        for row in product_rows:
            # Lấy tất cả các thẻ <td> trong hàng
            cells = row.find_elements(By.TAG_NAME, "td")

            if len(cells) > 0:
                try:
                    # Tìm thẻ input trong div.product-quantity (cột thứ 3) để lấy số lượng
                    input_element = cells[2].find_element(By.XPATH, ".//div[@class='product-quantity']/input[@type='number']")
                    quantity_value = int(input_element.get_attribute("value").strip())
                    
                    # Tính tổng giá tiền sản phẩm (cột thứ 5, thẻ <strong>)
                    price_str = cells[4].find_element(By.XPATH, ".//strong").text.strip()
                    # Xử lý giá tiền, loại bỏ dấu phẩy và ký hiệu tiền tệ (ví dụ "$")
                    price_value = float(price_str.replace(",", "").replace("$", ""))
                    
                    # Cộng vào tổng tiền
                    total_amount += price_value * quantity_value
                except Exception as e:
                    print(f"Lỗi khi lấy giá trị sản phẩm: {e}")
        
        # Hiển thị tổng tiền tính được từ các sản phẩm
        print(f"Tổng tiền tính từ các sản phẩm: {total_amount}")

        # So sánh tổng tiền hiển thị với tổng tiền tính được
        if abs(cart_amount - total_amount) < 1e-2:  # Kiểm tra với sai số nhỏ
            print("Tổng tiền trong checkout KHỚP với tổng tiền của các sản phẩm.")
        else:
            print(f"Tổng tiền trong checkout KHÔNG KHỚP. Tổng tiền checkout: {cart_amount}, tổng tiền sản phẩm: {total_amount}")
            
    except Exception as e:
        print(f"Lỗi khi xử lý giỏ hàng: {e}")

