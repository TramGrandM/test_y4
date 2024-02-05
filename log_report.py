import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogReport:
    def __init__(self, driver):
        self.driver = driver

    def log_report(self):
        print("START LOG REPORT")
        try:
            menu = WebDriverWait(self.driver, 10).until(    
                EC.presence_of_element_located((By.XPATH, '//li[@id="menu_5"]'))
            )
            menu.click()
            first_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@id="select2-ReportUserCustomerId-container"]'))
            )
            first_name.click()
            input_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]/input[@class="select2-search__field"]'))
            )
            input_field.send_keys('')
            input_field.send_keys(Keys.ENTER)
            start_time = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@id="ReportFrom"]'))
            )
            start_time.send_keys('2024-01-20')
            btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and @class="btn btn-danger pull-right"]'))
            )
            btn.click()
            time.sleep(3)
            ex_mess = 'この項目は必ず入力して下さい。'
            report_first_name = self.driver.find_elements(By.CSS_SELECTOR, 'lable[for="ReportUserCustomerId"].error')
            report_from_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="ReportFrom"].error')
            report_to_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="ReportTo"].error')
            if report_first_name or report_from_mess or report_to_mess or report_from_mess == ex_mess or report_to_mess == ex_mess or report_first_name == ex_mess:
                print('The printed message matches the expected message. This required')
            time.sleep(3)
            choice = int(input("Input 1 If you want to click :   カレンダー(横方向)\nInput 2 If you want to click :   カレンダー(縦方向)\nInput 3 If you want to click :   印刷\n"))
            calendar_hoz = self.driver.find_element(By.LINK_TEXT, 'カレンダー(横方向)')
            calendar_ver = self.driver.find_element(By.LINK_TEXT, 'カレンダー(縦方向)')
            print_btn = self.driver.find_element(By.LINK_TEXT, '印刷')
            if choice == 1:
                calendar_hoz.click()
            elif choice == 2:
                calendar_ver.click()
            elif choice == 3:
                print_btn.click()
            else:
                print("Invalid")
            time.sleep(5)
        except TimeoutException:
            print("TimeoutException")
        except NoSuchElementException:
            print("NoSuchElementException")
        except Exception as e:
            print("ERR:", e)
        finally:
            print("END LOG REPORT")
