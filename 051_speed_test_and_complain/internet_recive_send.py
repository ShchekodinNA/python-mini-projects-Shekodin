
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

SPEED_TRIGGER_MBps = 150
SYMB = "&"
OKLA_URL = "https://www.speedtest.net/"
SPD_TST_URL = "https://www.speedtest.net/"
STNRDT_TM = 0.5

class IntrntDtMnpltn:
    def __init__(self, chrm_dvr_pth: str ,vk_url:str, vk_login:str, vk_password:str):
        self.driver = webdriver.Chrome(service=Service(chrm_dvr_pth))
        self.okla_url = OKLA_URL
        self.test_symb = SYMB
        self.vk_url = vk_url
        self.vk_login = vk_login
        self.vk_password = vk_password
        # self.vk_url = vk_url

    def get_internet_speed(self) -> float:
        self.driver.get(SPD_TST_URL)
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        is_cont = True
        current_speed = ""
        while is_cont:
            time.sleep(STNRDT_TM*4)
            current_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
            if len(current_speed) > 1:
                is_cont = False

        return float(current_speed)

    def send_comment_into_vk(self, message:str):
        self.driver.get(self.vk_url)
        self.driver.find_element(By.CLASS_NAME, "quick_login_button").click()
        time.sleep(STNRDT_TM)
        self.driver.find_element(By.TAG_NAME, "input").send_keys(self.vk_login)
        time.sleep(STNRDT_TM)

        self.driver.find_element(By.CSS_SELECTOR, ".vkc__EnterLogin__button button").click()
        time.sleep(STNRDT_TM)
        self.driver.find_element(By.NAME, "password").send_keys(self.vk_password)
        time.sleep(STNRDT_TM)
        self.driver.find_element(By.CSS_SELECTOR, ".vkc__EnterPasswordNoUserInfo__buttonWrap button").click()
        time.sleep(STNRDT_TM*2)
        self.driver.find_element(By.CSS_SELECTOR, "#public_contacts div a").click()
        time.sleep(STNRDT_TM)
        self.driver.find_element(By.CSS_SELECTOR, "#profile_message_send span").click()
        time.sleep(STNRDT_TM)
        self.driver.find_element(By.ID, "mail_box_editable").send_keys(message)
        time.sleep(STNRDT_TM)
        self.driver.find_element(By.ID, "mail_box_send").click()
        self.driver.close()