import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        wrong_pass_mess = "ログインエラー！ パスワードが間違っています。"
        wrong_mess = "ログインエラー！ 入力したメールアドレス、もしくは、パスワードが間違っています。"
        print("START LOGIN")
        # email = input("Input email: ")
        # password = input("Input password: ")
        email = "nvhuu.grandm@gmail.com"
        password = "12345678"
        e_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="data[User][email]"].form-control.required'))
        )
        e_email.send_keys(email)
        e_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="data[User][password]"].form-control.required'))
        )
        e_password.send_keys(password)
        if email == "" or password == "":
            print("Required")
        else:
            button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-warning btn-lg" and @type="submit"]'))
            )
            button.click()
            time.sleep(3)
            alert = self.driver.find_elements(By.CSS_SELECTOR, 'div.alert.alert-error.alert-dismissible[role="alert"]')
            if alert:
                if alert[0].text == wrong_pass_mess:
                    print(alert[0].text)
                    print('wrong_pass_mess, The printed message matches the expected message.')
                elif alert[0].text == wrong_mess:
                    print('wrong email or password ,The printed message matches the expected message.')
                else:
                    print('Unknown alert message', alert[0].text)
            else:
                try:
                    ex_url = "https://y4-dev.genkimiru.jp/admin/customers/index"
                    assert ex_url == self.driver.current_url, "Login failed"
                except Exception as e:
                    print("ERR", e)
                    return False
                else:
                    print("Login successfully")
                    return True
                finally:
                    print("END LOGIN")

