import datetime as dt
import smtplib
import requests

STOCK = "TSLA"
LANGUAGE = "en"
COMPANY_NAME = "Tesla Inc"
NEWS_TRIGGER = 0
NEWS_ARTICLES_AMOUNT = 3

API_ALPHAVANTAGE_KEY = "_____"
API_ALPHAVANTAGE_END_POINT = "https://www.alphavantage.co/query"
FUNCTION_ALPHAVANTAGE = "TIME_SERIES_DAILY"
alphavantage_parameters = {
    "function": FUNCTION_ALPHAVANTAGE,
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": API_ALPHAVANTAGE_KEY,
    "searchIn": "title"
}

API_NEWSAPI_KEY = "__"
API_NEWSAPI_END_POINT = "https://newsapi.org/v2/everything"
newsapi_parameters = {
    "apiKey": API_NEWSAPI_KEY,
    "q": COMPANY_NAME,
    "language": LANGUAGE,
}

my_email = "___"
smtp_setting = "smtp.inbox.ru"
my_password = "_____"
final_addres = "__"

reslt_apgtge = requests.get(url=API_ALPHAVANTAGE_END_POINT, params=alphavantage_parameters)
reslt_apgtge.raise_for_status()
yesterday = dt.datetime.now().date()-dt.timedelta(1)
data_ystrd = reslt_apgtge.json()["Time Series (Daily)"][str(yesterday)]

clos_ystrd = float(data_ystrd["4. close"])
diff_ystrd = round((clos_ystrd - float(data_ystrd["1. open"]))/clos_ystrd*100, 2)
get_news_string = f"{STOCK}: "
if diff_ystrd > 0:
    get_news_string += f"\\/{abs(diff_ystrd)}\n"
else:
    get_news_string += f"\\/{abs(diff_ystrd)}\n"

if abs(diff_ystrd) > NEWS_TRIGGER:
    reslt_news = requests.get(url=API_NEWSAPI_END_POINT, params=newsapi_parameters)
    reslt_news.raise_for_status()
    news = reslt_news.json()["articles"][:NEWS_ARTICLES_AMOUNT]
    get_news_string += "\n".join([f"    Title: {artcl['title']}\n    Description: {artcl['url']}" for artcl in news])
    print(get_news_string)


with smtplib.SMTP(smtp_setting) as cnnctn:
    cnnctn.starttls()
    cnnctn.login(user=my_email, password=my_password)
    cnnctn.sendmail(from_addr=my_email,
                    to_addrs=final_addres,
                    msg=f"Subject: STOCK MARKET INFO\n\n{get_news_string}")

