import time
from selenium.webdriver.common.by import By
from test_y4.search_page import Search


class MotionHealthCheck:
    def __init__(self, driver):
        self.driver = driver

    def motion_health_check(self):
        print('MotionHealthCheck START')
        li_alert = self.driver.find_element(By.XPATH, '//a[contains(text(), "健康診断結果")]')
        li_alert.click()
        mess_nodata = 'テーブルにデータがありません'
        no_data = self.driver.find_elements(By.XPATH, "//td[contains(text(), 'テーブルにデータがありません')]")
        if no_data and mess_nodata in no_data[0].text:
            print("No data")
            self.driver.back()
            time.sleep(3)
        else:
            time.sleep(3)
            se = Search(self.driver)
            if se.search() is True:
                results = self.driver.find_elements(By.XPATH, '//div[@class="icheckbox_flat-green"]')
                count = len(results)
                print("Health check result:", count)
                item = int(input(f"Enter the quantity you want to select < {count}: "))
                time.sleep(5)
                try:
                    for i, result in enumerate(results, start=1):
                        if i > item:
                            break
                        result.click()
                        alert = self.driver.find_elements(By.XPATH, '//div[@id="swal2-content" and @class="swal2-content"]')
                        ex_mess = 'ー度に表示する最大レコード数は3つのみです。'
                        if alert and ex_mess in alert[0].text:
                            time.sleep(5)
                            print('The printed message matches the expected message')
                            btn_ok = self.driver.find_element(By.XPATH, '//button[@class="swal2-confirm swal2-styled"]')
                            btn_ok.click()
                except Exception as e:
                    print("ERR:", e)
                else:
                    time.sleep(5)
                    btn = self.driver.find_element(By.ID, 'actionButton')
                    btn.click()
                    time.sleep(10)
                    print("MotionHealthCheck successfully")
                finally:
                    print("MotionHealthCheck END")

