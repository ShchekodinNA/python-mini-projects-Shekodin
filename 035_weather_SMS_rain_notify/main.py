import datetime
import vonage
import requests
import os
MY_LAT = 55.606254
MY_LNG = 37.410751
api_key = os.environ.get("OWM_API_KEY")
UNITS = "metric"
MY_LANG = "en"
EXCLUDE = "minutely,daily,alerts,current"
HOURS_TO_CHECK = 12
phone_number = os.environ.get("PHONE_NUMB")



api_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "units": UNITS,
    "lang": MY_LANG,
    "exclude": EXCLUDE

}
rslt = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=api_params)
rslt.raise_for_status()
data = rslt.json()
check_hours = [data["hourly"][i] for i in range(HOURS_TO_CHECK)]
temp = 0
feels_like = 0
is_rain = False
for i in range(HOURS_TO_CHECK):
    current_hour = data["hourly"][i]
    temp += current_hour["temp"]
    feels_like += current_hour["feels_like"]
    if current_hour["weather"][0]["id"] < 600:
        is_rain = True

temp = round(temp / HOURS_TO_CHECK, 2)
feels_like = round(feels_like / HOURS_TO_CHECK, 2)
time_now = datetime.datetime.now()
out_string = f"Forecast {time_now.day}.{time_now.month}.{time_now.year}. {HOURS_TO_CHECK} hours from {time_now.hour}:00 " \
             f"\nDaylight temperature: {temp} \N{DEGREE SIGN}C" \
             f"\nDaylight feels like: {feels_like} \N{DEGREE SIGN}C\n" \
             f"Raining: {is_rain}"


client = vonage.Client(key=os.environ.get("VONAGE_KEY"), secret=os.environ.get("VONAGE_SECRET"))
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Nikita-weather",
        "to": phone_number,
        "text": out_string,
    }
)


if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")