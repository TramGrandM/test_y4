import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search(self):
        print("START SEARCH")
        # data_search = "nvhuu.grandm@gmail.com"
        data_search = input("Input data search: ")
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"].form-control.input-sm'))
        )
        search.send_keys(data_search)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        result = self.driver.find_elements(By.XPATH, "//td[contains(text(), '一致するレコードがありません')]")
        if result:
            print("FAIL: No data")
            return False
        else:
            # f_string insert the value of a variable into a string
            test = self.driver.find_elements(By.XPATH, f"//td[contains(text(), '{data_search}')]")
            if test:
                print("Search successfully")
                return True
        print("END SEARCH")
