import smtplib
from google_sheets import SheetyData
from bs4 import BeautifulSoup
import requests

SHEET_URLS = "https://api.sheety.co/e442c94048a965ded887c28ccdf2f161/aliSender/urls"
SHEET_RECIPIENTS = "https://api.sheety.co/e442c94048a965ded887c28ccdf2f161/aliSender/recipients"
SHEET_AUTH_TOKEN = "Bearer **************"
GGL_SHT = "https://docs.google.com/spreadsheets/d/1GiW1CsXxwdl142AhVc0FoOEznaFKa5g573mw4bnfYGM/edit#gid=0"
my_email = "************.ru"
smtp_setting = "s********ru"
my_password = "w*************g"

HTTP_STANDART_HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.141 YaBrowser/22.3.2.644 Yowser/2.5 Safari/537.36",
}

sheets_obj_url = SheetyData(token=SHEET_AUTH_TOKEN, api_end_point=SHEET_URLS)
sheets_obj_rec = SheetyData(token=SHEET_AUTH_TOKEN, api_end_point=SHEET_RECIPIENTS)

res_sht_urls = sheets_obj_url.get_rows()
res_sht_urls.raise_for_status()
srch_item_lst = res_sht_urls.json()["urls"]

res_sht_recip = sheets_obj_rec.get_rows()
res_sht_recip.raise_for_status()
rec_list = res_sht_recip.json()['recipients']
for sritm in srch_item_lst:
    current_url = sritm['url']
    result = requests.get(url=current_url, headers=HTTP_STANDART_HEADER)
    result.raise_for_status()
    soup = BeautifulSoup(result.text, features="html.parser")
    item_price = soup.find(name="span", class_="product-price-current").text
    price_only = float(item_price.split()[0].replace(",", "."))
    if len(sritm['name']) > 0:
        item_name = sritm['name']
    else:
        item_name = soup.find(name="h1", class_="Product_Name__productTitleText__hntp3").text
    if price_only <= float(sritm['priceRub']) and len(rec_list) > 0 and sritm['mustsend'] == 1:
        mes_header = f"\|/ Aliexpress LOW PRICE ALERT \|/ '{item_name}'"
        mes_body = f"On your wished item - {item_name} current price is {item_price}\n"\
            f'Edit your list on {GGL_SHT}\nBUY on {current_url}'
        for rec in rec_list:
            with smtplib.SMTP(smtp_setting) as cnnctn:
                cnnctn.starttls()
                cnnctn.login(user=my_email, password=my_password)
                cnnctn.sendmail(from_addr=my_email,
                                to_addrs=rec['email'],
                                msg=f"Subject: {mes_header}\n\n{mes_body}".encode("utf-8"))

