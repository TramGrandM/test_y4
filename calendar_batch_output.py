import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CalendarBatchOutput:
    def __init__(self, driver):
        self.driver = driver

    def calender_batch_output(self):
        print("Start CalendarBatchOutput")
        try:
            onclick_value = "openModal('CalendarModal', 'P');"
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@onclick=\"{onclick_value}\"]"))
            )
            button.click()
            time.sleep(3)
            start_date = self.driver.find_element(By.ID, 'CalendarFrom')
            start_date.send_keys('2024-01-20')
            end_date = self.driver.find_element(By.ID, 'CalendarTo')
            # end_date.send_keys('2024年01月16日')
            end_date.click()
            end_date.send_keys(Keys.ENTER)
            onclick_btn = "submitCalendarExport('submitCalendarBtn');"
            btn_submit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,  f"//button[@onclick=\"{onclick_btn}\"]"))
            )
            btn_submit.click()
            time.sleep(3)
            ex_mess = 'この項目は必ず入力して下さい。'
            report_from_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="CalendarFrom"].error')
            report_to_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="CalendarTo"].error')
            if report_from_mess or report_to_mess or report_from_mess == ex_mess or report_to_mess == ex_mess:
                print('The printed message matches the expected message. This required')
            time.sleep(5)
            btn_close = self.driver.find_element(By.XPATH, '//*[@id="CalendarModal"]/div/div/div[3]/button[2]')
            btn_close.click()
        except Exception as e:
            print("E:", e)
        finally:
            print("END CalendarBatchOutput")
