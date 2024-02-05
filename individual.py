import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Individual:
    def __init__(self, driver):
        self.driver = driver

    def individual(self):
        print("Start Individual")
        try:
            onclick_value = "openModal('AssessmentModal');"
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@onclick=\"{onclick_value}\"]"))
            )
            button.click()
            time.sleep(3)
            start_date = self.driver.find_element(By.ID, 'AssessmentFrom')
            start_date.send_keys('2024-02-01')
            end_date = self.driver.find_element(By.ID, 'AssessmentTo')
            # end_date.send_keys('2024年01月16日')
            end_date.click()
            end_date.send_keys(Keys.ENTER)
            # select item - div[1-2-3-4-5-6-7-8-9]
            item = self.driver.find_element(By.XPATH, '//*[@id="validate-assessment"]/div[2]/div[3]/div[5]/div/div')
            item.click()
            time.sleep(4)
            onclick_btn = "submitAssessmentExport('submitAssessmentBtn');"
            btn_submit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,  f"//button[@onclick=\"{onclick_btn}\"]"))
            )
            btn_submit.click()
            time.sleep(10)
            ex_mess = 'この項目は必ず入力して下さい。'
            report_from_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="AssessmentFrom"].error')
            report_to_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="AssessmentTo"].error')
            if report_from_mess or report_to_mess or report_from_mess == ex_mess or report_to_mess == ex_mess:
                print('The printed message matches the expected message. This required')
                time.sleep(5)
                btn_close = self.driver.find_element(By.XPATH, '//*[@id="AssessmentModal"]/div/div/div[3]/button[2]')
                btn_close.click()
        except Exception as e:
            print("E:", e)
        finally:
            print("END Individual")
