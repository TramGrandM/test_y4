import time
import os
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_y4.search_page import Search


class MotionEmail:
    def __init__(self, driver):
        self.driver = driver

    def motion_email(self):
        print("SEND EMAIL")
        li_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Email")]'))
        )
        li_email.click()
        time.sleep(2)
        title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="data[Report][title]" and @id="ReportTitle"]'))
        )
        c_title = input("Input title: ")
        title.send_keys(c_title)
        content = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="note-editable" and @contenteditable="true"]'))
        )
        c_content = input("Input content: ")
        content.send_keys(c_content)
        choose = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="data[Report][file]" and @id="ReportFile"]'))
        )

        file_path = r"C:\Users\TramGrandM\Downloads\aaaa.xlsx"
        cancle = self.driver.find_element(By.XPATH, '//*[@id="MailModal"]/div/div/div[3]/button[2]')
        try:
            if os.path.exists(file_path):
                choose.send_keys(file_path)
            else:
                print("File is not exist")
                cancle.click()
            btn_send = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@id="mailBtn"]'))
            )
            btn_send.click()
            ex_title = 'この項目は必ず入力して下さい。'
            alert_title = self.driver.find_elements(By.XPATH, '//*[@id="validate-2"]/div[2]/div/div/label')
            if alert_title and ex_title in alert_title[0].text:
                print("The printed message matches the expected message.Title is required")
                cancle.click()
            time.sleep(10)
        except Exception as e:
            print("ERR:", e)
        else:
            print("Send successfully")
        finally:
            print("END SEND EMAIL")

