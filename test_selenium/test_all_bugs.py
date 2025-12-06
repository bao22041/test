
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    return webdriver.Chrome(options=options)


def test_bug1_register_error(driver):
    print(" Test BUG1: Đăng ký thành công nhưng báo lỗi")
    driver.get("http://localhost:3000/signup")

    driver.find_element(By.NAME, "email").send_keys("thienbao2204@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("12345678")
    driver.find_element(By.NAME, "passwordConfirm").send_keys("12345678")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    time.sleep(2)

    error = driver.find_elements(By.XPATH, "//*[contains(text(), 'Registration failed')]")
    if error:
        print("  BUG1 tái hiện: Đăng ký thành công nhưng vẫn báo lỗi.")
    else:
        print("  BUG1 Passed: Không có lỗi đăng ký.")


def test_bug2_login_no_response(driver):
    print(" Test BUG2: Đăng nhập đúng nhưng không phản hồi")
    driver.get("http://localhost:3000/login")

    wait = WebDriverWait(driver, 15)

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Sign In')]")))

        # Nhập email
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys("bao3321@gmail.com")

        # Nhập mật khẩu
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.clear()
        password_input.send_keys("12345678")

        # Nhấn Sign In
        sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]")))
        sign_in_btn.click()

        time.sleep(2)

        if "dashboard" in driver.current_url or "home" in driver.current_url:
            print("  BUG2 Passed: Đăng nhập thành công.")
        else:
            print("  BUG2 tái hiện: Không chuyển trang sau đăng nhập đúng.")

    except Exception as e:
        print(f"  BUG2 lỗi không tìm thấy phần tử (đăng nhập): {e}")


def test_bug3_add_to_cart_not_clickable(driver):
    print(" Test BUG3: Nút Add To Cart không nhấn được")
    driver.get("http://localhost:3000/")

    try:
        wait = WebDriverWait(driver, 10)
        # Chờ nút "Add to cart" xuất hiện
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))

        if add_btn.is_enabled():
            add_btn.click()
            print("  BUG3 Passed: Nút Add To Cart hoạt động.")
        else:
            print("  BUG3 tái hiện: Nút Add To Cart bị vô hiệu.")
    except Exception as e:
        print(f"  BUG3 lỗi: {e}")


def test_bug4_short_password_allowed(driver):
    print(" Test BUG4: Cho phép đăng ký với mật khẩu quá ngắn")
    driver.get("http://localhost:3000/signup")

    driver.find_element(By.NAME, "email").send_keys("thienbao@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "passwordConfirm").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    time.sleep(2)

    error = driver.find_elements(By.XPATH, "//*[contains(text(), 'at least 8 characters')]")
    if error:
        print("  BUG4 Passed: Không cho đăng ký với mật khẩu ngắn.")
    else:
        print("  BUG4 tái hiện: Cho phép đăng ký với mật khẩu không hợp lệ.")


if __name__ == "__main__":
    driver = init_driver()
    try:
        test_bug1_register_error(driver)
        test_bug2_login_no_response(driver)
        test_bug3_add_to_cart_not_clickable(driver)
        test_bug4_short_password_allowed(driver)
    finally:
        driver.quit()
