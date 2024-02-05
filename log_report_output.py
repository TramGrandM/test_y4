import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogReportOutput:
    def __init__(self, driver):
        self.driver = driver

    def log_report_output(self):
        print("START LOG REPORT OUTPUT")
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "actionButton"))
            )
            button.click()
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, "input.select2-search__field").click()
            time.sleep(3)
            # select log type
            log_type = self.driver.find_element(By.XPATH, "//li[. = '体重']")
            log_type.click()
            time.sleep(2)
            start_date = self.driver.find_element(By.ID, 'ReportFrom')
            start_date.send_keys('2024年01月18日')
            end_date = self.driver.find_element(By.ID, 'ReportTo')
            end_date.send_keys('2024年01月18日' + Keys.ENTER)
            # end_date.send_keys(Keys.ENTER)
            choice = input("Input 1 If you want to click :  CSV形一括出力\nInput 2 If you want to click :  エクセル形一括出力\nInput 3 If you want to click :  個別出力\n")
            btn1 = self.driver.find_element(By.ID, 'submitBtn3')
            btn2 = self.driver.find_element(By.ID, 'submitBtn2')
            btn3 = self.driver.find_element(By.ID, 'submitBtn')
            if choice == '1':
                btn1.click()
                time.sleep(1)
            elif choice == '2':
                btn2.click()
                time.sleep(1)
            elif choice == '3':
                btn3.click()
                time.sleep(1)
            else:
                print("Failed")
            ex_mess = 'この項目は必ず入力して下さい。'
            report_from_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="ReportFrom"].error')
            report_to_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="ReportTo"].error')
            if report_from_mess or report_to_mess or report_from_mess == ex_mess or report_to_mess == ex_mess:
                print('The printed message matches the expected message. This required')
                time.sleep(5)
                close = self.driver.find_element(By.XPATH, '//*[@id="MessageModal"]/div/div/div[3]/button[4]')
                close.click()
            time.sleep(3)
        except Exception as e:
            print("E:", e)
        finally:
            print("END LOG REPORT OUTPUT")
