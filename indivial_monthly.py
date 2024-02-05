import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndividualMonthly:
    def __init__(self, driver):
        self.driver = driver

    def individual_monthly(self):
        print("Start IndividualMonthly")
        try:
            onclick_value = "openModal('AssessmentByMonthModal');"
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@onclick=\"{onclick_value}\"]"))
            )
            button.click()
            time.sleep(3)
            start_date = self.driver.find_element(By.ID, 'AssessmentByMonthFrom')
            start_date.send_keys('2024-02-01')
            # select item - div[1-2-3-4-5-6-7-8-9]
            # print("c")
            # item = self.driver.find_element(By.XPATH, '//*[@id="validate-assessmentbymonth"]/div[3]/div/div[1]/div/div')
            # print("DD")
            # item.click()
            # print("E")
            # time.sleep(4)
            onclick_btn = "submitAssessmentExportByMonth('submitAssessmentByMonthBtn');"
            btn_submit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,  f"//button[@onclick=\"{onclick_btn}\"]"))
            )
            btn_submit.click()
            time.sleep(10)
            ex_mess = 'この項目は必ず入力して下さい。'
            report_from_mess = self.driver.find_elements(By.CSS_SELECTOR, 'label[for="AssessmentByMonthFrom"].error')

            if report_from_mess or report_from_mess == ex_mess:
                print('The printed message matches the expected message. This required')
                time.sleep(5)
                btn_close = self.driver.find_element(By.XPATH, '//*[@id="AssessmentByMonthModal"]/div/div/div[3]/button[2]')
                btn_close.click()
        except Exception as e:
            print("E:", e)
        else:
            print("IndividualMonthly successfully")
        finally:
            print("END IndividualMonthly")
