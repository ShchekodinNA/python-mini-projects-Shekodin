import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrm_dvr_pth = "F:\dev\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrm_dvr_pth))

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
while True:

    cookie = driver.find_element(By.ID, "bigCookie")
    for _ in range(350):
        cookie.click()
    try:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades div")
        for upg in upgrades:
            upg.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        pass
    prods = driver.find_elements(By.CSS_SELECTOR, "#products .unlocked")
    prods.reverse()
    for prd in prods:
        prd.click()


