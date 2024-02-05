import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import Login
from search_page import Search
from action_page import Action
from log_report_output import LogReportOutput
from checkin_detail import CheckinDetail
from calendar_batch_output import CalendarBatchOutput
from batch_calendar_output import BatchCalendarOutput
from renpho import Renpho
from individual import Individual
from indivial_monthly import IndividualMonthly
from alert_selection import AlertSelection
from motion.motion import Motion
from motion.motion_email import MotionEmail
from motion.motion_health_check import MotionHealthCheck

from log_report import LogReport

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://y4-dev.genkimiru.jp/")

# driver.find_element(By.XPATH, f'//a[@href="/users/signup" and @class="to_register"]').click()

login = Login(driver)
search = Search(driver)
action = Action(driver)
log = LogReportOutput(driver)
checkin = CheckinDetail(driver)
calendar = CalendarBatchOutput(driver)
batch = BatchCalendarOutput(driver)
renpho = Renpho(driver)
individual = Individual(driver)
individual_monthly = IndividualMonthly(driver)
alertselection = AlertSelection(driver)
# Motion
motion = Motion(driver)
email = MotionEmail(driver)
healthcheck = MotionHealthCheck(driver)
# Log report
log_report = LogReport(driver)

"""
if login.login() is True:
    a = Action(driver)
    a.action()
"""
if login.login() is True:
    # log_report.log_report()
    if search.search() is True:
        # - motion
        # motion.motion()
        # email.motion_email()
        motion.motion()
        healthcheck.motion_health_check()
        # - action
        # action.action()
        # log.log_report_output()
        # checkin.checkin_detail()
        # calendar.calender_batch_output()
        # batch.batch_calender_output()
        # renpho.renpho()
        # individual.individual()
        # individual_monthly.individual_monthly()
        # alertselection.alert_selection()

driver.quit()
