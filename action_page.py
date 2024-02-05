import time
from selenium.webdriver.common.by import By
# select user


class Action:
    def __init__(self, driver):
        self.driver = driver

    def action(self):
        # tr = self.driver.find_element(By.XPATH, '//input[@type="checkbox" and @class="dt-checkboxes" and @wfd-id="id73"]')
        try:
            # table = self.driver.find_element(By.XPATH, '//table[@id="DataTables_Table_0"]')
            td_element = self.driver.find_element(By.XPATH, ".//tr[1]/td[1]")
            td_element.click()
            time.sleep(3)
            """checkbox = self.driver.find_element(By.XPATH, '//input[@type="checkbox" and @class="dt-checkboxes" and @wfd-id="id49"]')
            time.sleep(5)
            checkbox.click()"""
        except Exception as e:
            print(e)
        else:
            print("OK")
        finally:
            print("END")
