import requests
from datetime import datetime
import smtplib
import time

my_email = "apot69@inbox.ru"
to_email = "kacpercku10971@gmail.com"
smtp_setting = "smtp.inbox.ru"
my_password = "wg2QYEpcsHXzkr7Xt4Rg"

MY_LAT = 55.606254
MY_LONG = 37.410751
GMT = 3

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_nght(your_hour, sun_rise, sun_set) ->bool:
    if your_hour < sun_rise or your_hour > sun_set:
        return True
    return False


while True:
    time.sleep(60)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    is_overhead = False
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 or iss_longitude - 5 <= MY_LONG <= iss_longitude:
        is_overhead = True
    if not is_overhead: continue
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+GMT
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])+GMT
    is_night = False
    hour_now = datetime.now().hour
    if is_nght(hour_now, sunrise, sunset):
        with smtplib.SMTP(smtp_setting) as cnnctn:
            cnnctn.starttls()
            cnnctn.login(user=my_email, password=my_password)
            cnnctn.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:ISS overhead\n\nDon't read, look at sky!")





