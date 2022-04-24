from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SRCH_JOB = "Python developer"
SRCH_REG = "Moscow, Russia"

LINK_LOGIN = "k**************"
LINK_PASSW = "************"
LINK_BEGIN_URL = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

chrm_dvr_pth = "F:\dev\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrm_dvr_pth))

driver.get(LINK_BEGIN_URL)

username_obj = driver.find_element(By.ID, "username")
password_obj = driver.find_element(By.ID, "password")
btn_obj = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
username_obj.send_keys(LINK_LOGIN)
password_obj.send_keys(LINK_PASSW)
btn_obj.click()
time.sleep(1)
btn_obj = driver.find_element(By.CSS_SELECTOR, "#ember19 svg use")

btn_obj.click()
time.sleep(0.5)

inputs = driver.find_elements(By.CLASS_NAME, "jobs-search-box__text-input")
inputs[0].send_keys(SRCH_JOB)
time.sleep(0.2)
inputs[3].send_keys(SRCH_REG)
time.sleep(0.2)
inputs[3].send_keys(Keys.ENTER)
time.sleep(3)
current_page = 0

pages = driver.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__indicator")
max_len = len(pages)
for pg in range(0, max_len):
    pages[pg].click()
    time.sleep(0.5)
    pages = driver.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__indicator")
    work_items = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
    print(len(work_items))
    for i in work_items:
        i.click()
        time.sleep(0.6)
        btn_save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        btn_save.click()

