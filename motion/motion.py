import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Motion:
    def __init__(self, driver):
        self.driver = driver

    def motion(self):
        td_element = self.driver.find_element(By.XPATH, ".//tr[1]/td[12]")
        td_element.click()
        time.sleep(3)
