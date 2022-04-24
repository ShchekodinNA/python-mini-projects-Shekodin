import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

STNDRT_SCRL = 125
WRNG_URL = "WrongUrl"

class ZilRes:
    def __init__(self, chrm_dvr_pth: str, zillo_srch_url: str):
        self.driver = webdriver.Chrome(service=Service(chrm_dvr_pth))
        self.zillo_srch_url = zillo_srch_url

    def get_data_from_zillo(self):
        try:
            self.driver.get(self.zillo_srch_url)
        except selenium.common.exceptions.WebDriverException:
            return WRNG_URL
        time.sleep(3)
        current_data = self.driver.find_elements(By.CSS_SELECTOR, ".photo-cards li")
        table = []
        self.driver.execute_script("window.scrollTo(0, 9000)")
        for i in range(len(current_data)):
            try:
                time.sleep(0.05)
                crnt_url = current_data[i].find_element(By.TAG_NAME, "a")
                current_price = current_data[i].find_element(By.CLASS_NAME, "list-card-price").text
                current_price = current_price.split("/")[0]
                current_price = current_price.split("+")[0]
                dict_item = {
                    "address": crnt_url.find_element(By.TAG_NAME, "address").text,
                    "price": current_price,
                    "url": crnt_url.get_attribute(name="href"),
                }
                self.driver.execute_script(f"window.scrollTo(0, {i * STNDRT_SCRL})")
                table.append(dict_item)
            except selenium.common.exceptions.NoSuchElementException:
                pass
        return table

    def fill_ggl_frms(self, table: list, ggl_frms_ref: str, sequence_fill=(0, 1, 2)):

        for row in table:
            try:
                self.driver.get(ggl_frms_ref)
            except selenium.common.exceptions.WebDriverException:
                return WRNG_URL
            inputs = self.driver.find_elements(By.CSS_SELECTOR, ".Qr7Oae input")
            inputs[sequence_fill[0]].send_keys(row["address"])
            inputs[sequence_fill[1]].send_keys(row["price"])
            inputs[sequence_fill[2]].send_keys(row["url"])
            self.driver.find_element(By.CLASS_NAME, "NPEfkd").click()

    def close_windows(self):
        self.driver.close()