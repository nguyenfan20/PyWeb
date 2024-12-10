import random
from .driver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Test thêm 1 sản phẩm vào giỏ hàng

def test_add_to_cart(driver):
    valid_account(driver)  # Kiểm tra tài khoản
    driver.get("http://127.0.0.1:5000/product-list")
    time.sleep(2)  # Đợi để trang tải hoàn toàn sau khi đăng nhập
    print("Đăng nhập thành công, bắt đầu kiểm tra sản phẩm...")

    try:
        product_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "row.product-list"))
        )
        print(f"Số lượng phần tử trong product_list: {len(product_list)}")

        # Kiểm tra nếu product_list không rỗng
        if product_list:
            # Chọn ngẫu nhiên một sản phẩm từ danh sách sản phẩm
            product_items = product_list[0].find_elements(
                By.CLASS_NAME, "col-md-4") 
            # Chọn sản phẩm ngẫu nhiên
            selected_item = random.choice(product_items)

            # Tìm thẻ <a> trong thẻ <h3> chứa tên sản phẩm
            product_detail_link = selected_item.find_element(
                By.CSS_SELECTOR, "h3 a[href]").get_attribute("href")
            print(f"Đang truy cập vào trang chi tiết sản phẩm: {product_detail_link}")

            # Truy cập vào trang chi tiết sản phẩm
            driver.get(product_detail_link)
            time.sleep(3)  # Đợi để trang chi tiết sản phẩm tải
            try:
                # Lấy tên sản phẩm từ trang chi tiết sản phẩm
                # Tên sản phẩm thường nằm trong thẻ <h1>
                product_name = driver.find_element(By.TAG_NAME, "h1").text
                print(f"Tên sản phẩm: {product_name}")

                # Lấy giá sản phẩm từ thẻ <strong> (chỉ lấy giá trong thẻ <strong>)
                price_block = driver.find_element(
                    By.CLASS_NAME, "price-availability-block")
                product_price = price_block.find_element(
                    By.TAG_NAME, "strong").text
                print(f"Giá sản phẩm: {product_price}")

                # Tiến hành thao tác thêm vào giỏ hàng
                # Tìm lại nút "Add to cart" sau khi thay đổi DOM
                add_to_cart_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".product-page-cart a.btn.btn-primary.add2cart"))
                )
                add_to_cart_button.click()  # Nhấn vào nút "Add to cart"
                # truy cập vào giỏ hàng
                cart_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".top-cart-block a[href] i.fa-shopping-cart"))
                )
                cart_link.click()  # Nhấn vào giỏ hàng
                time.sleep(3)

                # Kiểm tra thông tin trong giỏ hàng
                cart_items = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR,
                         "div.table-wrapper-responsive table[summary='Shopping cart'] tbody tr")
                    )
                )

                if len(cart_items) >= 2:
                    cart_item = cart_items[1]
                    # print(f"Cart item content: {cart_item.text}")
                    product_name_in_cart = cart_item.find_element(
                        By.CSS_SELECTOR, ".goods-page-description h3 a").text
                    print(f"tên sp trong giỏ: {product_name_in_cart}")

                    product_price_in_cart = cart_item.find_element(
                        By.CSS_SELECTOR, ".goods-page-price strong").text
                    print(f"giá sp trong giỏ: {product_price_in_cart}")

                    # Chuẩn hóa tên sản phẩm (bỏ khoảng trắng thừa và chuyển thành chữ thường)
                    product_name = product_name.strip().lower()
                    product_name_in_cart = product_name_in_cart.strip().lower()

                    # Chuẩn hóa giá sản phẩm (loại bỏ ký tự $, chuyển thành float)
                    product_price = float(
                        product_price.replace("$", "").strip())
                    product_price_in_cart = float(
                        product_price_in_cart.replace("$", "").strip())

                    if product_name_in_cart == product_name and product_price_in_cart == product_price:
                        print("Thông tin sản phẩm trong giỏ hàng chính xác.")
                    else:
                        print(f"Lỗi: Tên hoặc giá sản phẩm không khớp.")
                else:
                    print("Giỏ hàng không có sản phẩm nào.")
            except Exception as e:
                print(f"Lỗi khi lấy thông tin sản phẩm: {e}")

        else:
            print("Không tìm thấy sản phẩm trong danh sách.")

    except Exception as e:
        print(f"Không thể tìm thấy sản phẩm: {e}")


def test_add_multiple_products_to_cart(driver):
    valid_account(driver)  # Kiểm tra tài khoản
    driver.get("http://127.0.0.1:5000/product-list")
    time.sleep(2)  # Đợi để trang tải hoàn toàn sau khi đăng nhập
    print("Đăng nhập thành công, bắt đầu kiểm tra sản phẩm...")

    try:
        product_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "row.product-list"))
        )

        # Kiểm tra nếu product_list không rỗng
        if product_list:
            # Chọn các sản phẩm ngẫu nhiên từ danh sách sản phẩm
            product_items = product_list[0].find_elements(By.CLASS_NAME, "col-md-4")  
            selected_items = random.sample(product_items, 5)  # Chọn 5 sản phẩm ngẫu nhiên
            added_products = []
            # Lưu đường dẫn chi tiết và product-id của các sản phẩm
            product_detail_links = []
            for selected_item in selected_items:
                product_detail_link = selected_item.find_element(
                    By.CSS_SELECTOR, "h3 a[href]").get_attribute("href")
                product_detail_links.append(product_detail_link)
                print(f"Lưu đường dẫn chi tiết sản phẩm: {product_detail_link}")

            # Duyệt qua từng sản phẩm và thực hiện thao tác "thêm vào giỏ hàng"
            for product_detail_link in product_detail_links:
                print(f"Đang truy cập vào trang chi tiết sản phẩm: {product_detail_link}")
                driver.get(product_detail_link)
                time.sleep(3)  # Đợi để trang chi tiết sản phẩm tải
                try:
                    # Lấy tên sản phẩm và giá sản phẩm
                    product_name = driver.find_element(By.TAG_NAME, "h1").text
                    print(f"Tên sản phẩm: {product_name}")

                    price_block = driver.find_element(By.CLASS_NAME, "price-availability-block")
                    product_price = price_block.find_element(By.TAG_NAME, "strong").text

                    # Loại bỏ ký tự '$' và chuyển đổi giá trị thành float
                    product_price = product_price.replace("$", "").strip()
                    product_price = float(product_price)  # Chuyển đổi thành float
                    print(f"Giá sản phẩm: {product_price}")
                    
                    # Lấy product-id từ URL của sản phẩm
                    product_id = product_detail_link.split("product-id=")[-1]
                    print(f"product-id: {product_id}")

                    # Lưu thông tin sản phẩm vào danh sách added_products
                    added_products.append({
                        "id": product_id,
                        "name": product_name.strip().lower(), 
                        "price": product_price
                    })

                    # Tiến hành thao tác thêm vào giỏ hàng
                    add_to_cart_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, ".product-page-cart a.btn.btn-primary.add2cart"))
                    )
                    add_to_cart_button.click()  # Nhấn vào nút "Add to cart"
                    time.sleep(1)  # Đợi một chút trước khi chuyển sang sản phẩm tiếp theo

                    # Quay lại trang danh sách sản phẩm
                    driver.back()
                    time.sleep(3)  # Đợi để trang danh sách sản phẩm tải lại

                except Exception as e:
                    print(f"Lỗi khi lấy thông tin sản phẩm: {e}")

            # Truy cập vào giỏ hàng và kiểm tra thông tin
            cart_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".top-cart-block a[href] i.fa-shopping-cart"))
            )
            cart_link.click()  # Nhấn vào giỏ hàng
            time.sleep(3)
            # Kiểm tra sản phẩm trong giỏ hàng
            cart_rows = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR,"div.table-wrapper-responsive table[summary='Shopping cart'] tbody tr")
                )
            )

             # Bỏ qua tiêu đề (thẻ <th>)
            cart_items = cart_rows[1:]  # Bắt đầu từ thẻ <tr> thứ hai

            if len(cart_items) >= len(added_products):
                for i, cart_item in enumerate(cart_items[:len(added_products)]):
                    try:
                        # Lấy các cột trong mỗi sản phẩm của giỏ hàng
                        cart_columns = cart_item.find_elements(By.TAG_NAME, "td")  # Lấy tất cả các thẻ <td>

                        # Lấy tên sản phẩm trong giỏ hàng
                        cart_name = cart_columns[1].find_element(By.CSS_SELECTOR, ".goods-page-description h3 a").text.strip().lower()
                        print(f"Tên sản phẩm trong giỏ: {cart_name}")
                        # Lấy giá sản phẩm trong giỏ hàng
                        cart_price = cart_columns[3].find_element(By.CSS_SELECTOR, ".goods-page-price strong").text
                        print(f"Giá sản phẩm trong giỏ: {cart_price}")
                        cart_price = float(cart_price.replace("$", "").strip())  # Chuyển giá thành float

                        # Lấy product-id từ sản phẩm trong giỏ hàng
                        cart_product_id = cart_columns[1].find_element(By.CSS_SELECTOR, "a").get_attribute("href").split("product-id=")[-1]

                        # Lấy thông tin sản phẩm đã lưu từ added_products
                        expected_product = added_products[i]

                        # So sánh product-id, tên và giá sản phẩm trong giỏ hàng với sản phẩm đã thêm
                        for expected_product in added_products:
                            if cart_product_id == expected_product["id"]:  # Nếu ID khớp
                                if cart_name == expected_product["name"] and cart_price == expected_product["price"]:
                                    print(f"Sản phẩm đúng: {cart_name} - ${cart_price}")
                                else:
                                    print(f"Lỗi: Sản phẩm không khớp.\n"
                                        f"  Giỏ hàng: {cart_name} - ${cart_price}\n"
                                        f"  Dự kiến: {expected_product['name']} - ${expected_product['price']}")
                                break  # Dừng kiểm tra sản phẩm hiện tại trong giỏ hàng vì đã tìm thấy khớp
                        else:
                            print(f"Lỗi: Không tìm thấy sản phẩm với ID {cart_product_id} trong danh sách đã thêm.")
                    except Exception as e:
                        print(f"Lỗi khi so sánh sản phẩm {i+1}: {e}")
            else:
                print("Giỏ hàng không đủ sản phẩm đã thêm.")

    except Exception as e:
        print(f"Không thể tìm thấy sản phẩm: {e}")