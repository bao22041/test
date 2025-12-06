from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


BASE_URL = "http://localhost:3000"

class TestWebsite:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def _navigate_to(self, url):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Đã điều hướng đến: {url}")

    def _find_element(self, by, value, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except:
            print(f"Hết thời gian chờ: Không tìm thấy phần tử theo {by}='{value}'")
            return None

    def _click_element(self, by, value, timeout=10):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            el.click()
            print(f"Đã click vào phần tử theo {by}='{value}'")
            return True
        except:
            print(f"Không thể click vào phần tử theo {by}='{value}'")
            return False

    def _check_text_present(self, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text)
            )
            return True
        except:
            return False

    # TC001: Đăng ký tài khoản
    def test_tc001_register_account(self):
        print("\n--- TC001: Đăng ký tài khoản ---")
        self._navigate_to(f"{BASE_URL}/signup")
        email = self._find_element(By.NAME, "email")
        password = self._find_element(By.NAME, "password")
        confirm = self._find_element(By.NAME, "passwordConfirm")
        signup_btn = self._find_element(By.XPATH, "//button[text()='Sign Up']")

        if not all([email, password, confirm, signup_btn]):
            return "Thất bại"

        email.send_keys("testuser123@example.com")
        password.send_keys("TestPassword123")
        confirm.send_keys("TestPassword123")
        signup_btn.click()
        time.sleep(2)

        if self._check_text_present("Registration success"):
            return "Đạt"
        elif self._check_text_present("failed"):
            return "Thất bại"
        return "Thất bại"

    # TC002: Đăng nhập
    def test_tc002_login_functionality(self):
        print("\n--- TC002: Đăng nhập ---")
        self._navigate_to(f"{BASE_URL}/signin")
        email = self._find_element(By.NAME, "email")
        password = self._find_element(By.NAME, "password")
        signin = self._find_element(By.XPATH, "//button[text()='Sign In']")

        if not all([email, password, signin]):
            return "Thất bại"

        email.send_keys("bao1@gmail.com")
        password.send_keys("123456789")
        signin.click()
        time.sleep(2)

        if "home" in self.driver.current_url or "dashboard" in self.driver.current_url:
            return "Đạt"
        return "Thất bại"

    # TC003: Hiển thị trang chủ
    def test_tc003_homepage_display(self):
        print("\n--- TC003: Trang chủ hiển thị ---")
        self._navigate_to(BASE_URL)
        product_card = self._find_element(By.CLASS_NAME, "chakra-card")
        return "Đạt" if product_card else "Thất bại"

    # TC004: Add to cart
    def test_tc004_add_to_cart(self):
        print("\n--- TC004: Add to cart ---")
        self._navigate_to(BASE_URL)
        self._click_element(By.XPATH, "//button[text()='Add to cart']")
        time.sleep(2)
        if self._check_text_present("added to cart") or self._check_text_present("Basket (1)"):
            return "Đạt"
        return "Thất bại"

    # TC005: Add to basket
    def test_tc005_add_to_basket(self):
        print("\n--- TC005: Add to basket ---")
        self._navigate_to(BASE_URL)
        self._click_element(By.XPATH, "//button[text()='Add to Basket']")
        time.sleep(2)
        basket_btn = self._find_element(By.XPATH, "//button[contains(text(),'Basket')]")
        return "Đạt" if basket_btn and "1" in basket_btn.text else "Thất bại"

    # TC006: Xóa khỏi basket
    def test_tc006_remove_from_basket(self):
        print("\n--- TC006: Xóa khỏi basket ---")
        self.test_tc005_add_to_basket()
        self._navigate_to(f"{BASE_URL}/basket")
        time.sleep(2)
        self._click_element(By.XPATH, "//button[contains(text(),'Remove')]")
        time.sleep(2)
        return "Đạt" if self._check_text_present("Your basket is empty") else "Thất bại"

    # TC007: Hiển thị chi tiết sản phẩm
    def test_tc007_product_detail_display(self):
        print("\n--- TC007: Chi tiết sản phẩm ---")
        self._navigate_to(f"{BASE_URL}/product/683a64200804f6c894157a33") #suawr cho nay
        product_link = self._find_element(By.XPATH, "//a[contains(@href, '/product/')]")
        if not product_link:
            return "Thất bại"
        self.driver.get(product_link.get_attribute("href"))
        time.sleep(2)
        return "Đạt" if self._find_element(By.XPATH, "//button[text()='Add to cart']") else "Thất bại"

    # TC008: Đăng ký với email đã tồn tại
    def test_tc008_register_existing_email(self):
        print("\n--- TC008: Email đã tồn tại ---")
        self._navigate_to(f"{BASE_URL}/signup")
        email = self._find_element(By.NAME, "email")
        password = self._find_element(By.NAME, "password")
        confirm = self._find_element(By.NAME, "passwordConfirm")
        signup_btn = self._find_element(By.XPATH, "//button[text()='Sign Up']")

        if not all([email, password, confirm, signup_btn]):
            return "Thất bại"

        email.send_keys("bao105497@donga.edu.vn")
        password.send_keys("12345678")
        confirm.send_keys("12345678")
        signup_btn.click()
        time.sleep(2)

        return "Đạt" if self._check_text_present("already using") else "Thất bại"

    # TC009: Mật khẩu < 8 ký tự
    def test_tc009_register_short_password(self):
        print("\n--- TC009: Mật khẩu ngắn ---")
        self._navigate_to(f"{BASE_URL}/signup")
        email = self._find_element(By.NAME, "email")
        password = self._find_element(By.NAME, "password")
        confirm = self._find_element(By.NAME, "passwordConfirm")
        signup_btn = self._find_element(By.XPATH, "//button[text()='Sign Up']")

        if not all([email, password, confirm, signup_btn]):
            return "Thất bại"

        email.send_keys("shortpass@example.com")
        password.send_keys("short")
        confirm.send_keys("short")
        signup_btn.click()
        time.sleep(2)

        if self._check_text_present("at least 8 characters"):
            return "Đạt"
        return "Thất bại"

    # TC010: Hiển thị email profile
    def test_tc010_account_info_display(self):
        print("\n--- TC010: Thông tin tài khoản ---")
        if self.test_tc002_login_functionality() != "Đạt":
            return "Bỏ qua"
        self._navigate_to(f"{BASE_URL}/profile")
        return "Đạt" if self._check_text_present("bao1@gmail.com") else "Thất bại"

    # TC011: Thêm nhiều sản phẩm vào giỏ
    def test_tc011_cart_with_multiple_products(self):
        print("\n--- TC011: Giỏ hàng nhiều sản phẩm ---")
        self._navigate_to(BASE_URL)
        btns = self.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        if len(btns) < 2:
            return "Bỏ qua"
        btns[0].click()
        time.sleep(1)
        btns[1].click()
        time.sleep(2)
        self._navigate_to(f"{BASE_URL}/cart")
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        return "Đạt" if len(items) >= 2 else "Thất bại"

    # TC012: Giỏ hàng trống
    def test_tc012_empty_cart(self):
        print("\n--- TC012: Giỏ hàng trống ---")
        self._navigate_to(f"{BASE_URL}/basket")
        return "Đạt" if self._check_text_present("You have not any items in your basket") else "Thất bại"

    # TC013: Tốc độ tải trang
    def test_tc013_page_load_speed(self):
        print("\n--- TC013: Tốc độ tải trang ---")
        start = time.time()
        self._navigate_to(BASE_URL)
        elapsed = time.time() - start
        return "Đạt" if elapsed < 5 else "Thất bại"

    # TC014: Đăng xuất
    def test_tc014_logout_functionality(self):
        print("\n--- TC014: Đăng xuất ---")
        if self.test_tc002_login_functionality() != "Đạt":
            return "Bỏ qua"
        self._navigate_to(f"{BASE_URL}/profile")
        return "Đạt" if self._click_element(By.XPATH, "//button[text()='Logout']") else "Thất bại"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    test = TestWebsite()
    results = {
        "TC001": test.test_tc001_register_account(),
        "TC002": test.test_tc002_login_functionality(),
        "TC003": test.test_tc003_homepage_display(),
        "TC004": test.test_tc004_add_to_cart(),
        "TC005": test.test_tc005_add_to_basket(),
        "TC006": test.test_tc006_remove_from_basket(),
        "TC007": test.test_tc007_product_detail_display(),
        "TC008": test.test_tc008_register_existing_email(),
        "TC009": test.test_tc009_register_short_password(),
        "TC010": test.test_tc010_account_info_display(),
        "TC011": test.test_tc011_cart_with_multiple_products(),
        "TC012": test.test_tc012_empty_cart(),
        "TC013": test.test_tc013_page_load_speed(),
        "TC014": test.test_tc014_logout_functionality()
    }

    print("\n--- TÓM TẮT KẾT QUẢ ---")
    for k, v in results.items():
        print(f"{k}: {v}")
    test.tearDown()
