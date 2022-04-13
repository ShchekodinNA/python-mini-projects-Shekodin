import smtplib

from data_manager import SheetyData
from flight_data import FlightData
import datetime as dt
from dateutil.relativedelta import relativedelta
MY_CITY_IATA = "LON"
NGHTS_MIN = 2
NGHTS_MAX = 6
SRCH_MNTH_IN_FUTURE = 6
DATE_FORMAT_STRING = "%d/%m/%Y"
SHEETY_TOKEN = "Bearer YOUR"
SHEETY_END_POINT = "YOUR"

TEQUILA_END_POINT = "https://tequila-api.kiwi.com"
TEQUILA_APIKEY = "YOUR"

my_email = "YOUR"
smtp_setting = "smtp.inbox.ru"
my_password = "YOUR"
final_addres = "YOUR"



sheety_data = SheetyData(token=SHEETY_TOKEN, api_end_point=SHEETY_END_POINT)

tequila_data = FlightData(end_point=TEQUILA_END_POINT, apikey=TEQUILA_APIKEY)
retrive_rows = sheety_data.get_rows()
rows = retrive_rows.json()["prices"]

# for i in range(len(rows)):
#     current_row = rows[i]
#     cit_name = current_row["city"]
#     srch_res_obj = tequila_data.get_iata_city(city_name=cit_name)
#     srch_res_obj.raise_for_status()
#     city_iata = srch_res_obj.json()
#     if  current_row['iataCode'] == "":
#         current_row['iataCode'] = city_iata
#         info = sheety_data.update_row(chng_rw_id=current_row["id"], body_json={"price": current_row})
current_date = dt.date.today().strftime(DATE_FORMAT_STRING )
to_date = (dt.date.today() + relativedelta(months=SRCH_MNTH_IN_FUTURE)).strftime(DATE_FORMAT_STRING)

for i in range(len(rows)):
    current_row = rows[i]
    price_srch = tequila_data.get_flights(
        from_iata=MY_CITY_IATA,
        to_iata=current_row['iataCode'],
        srch_frm_dt=current_date,
        srch_to_dt=to_date,
        nights_in_min=NGHTS_MIN,
        nights_in_max=NGHTS_MAX
    )
    price_srch.raise_for_status()
    price = price_srch.json()["data"][0]
    print(f"{current_row['city']}: {price} eur")
    my_price_trashhold = current_row['lowestPrice']
    if price["price"] <= my_price_trashhold:
        from_date = dt.date.fromtimestamp(price['route'][0]['aTimeUTC'])
        to_date = dt.date.fromtimestamp(price['route'][-1]['aTimeUTC'])
        mail_head = "Low price alert!"
        mail_body = f"Only {price['price']} euros to fly from {price['cityFrom']}-{price['flyFrom']}" \
                    f"to {price['cityTo']}-{price['flyTo']}. {price['nightsInDest']} Nights.\n" \
                    f"from utc {from_date } to {to_date}."
        with smtplib.SMTP(smtp_setting) as cnnctn:
            cnnctn.starttls()
            cnnctn.login(user=my_email, password=my_password)
            cnnctn.sendmail(from_addr=my_email,
                            to_addrs=final_addres,
                            msg=f"Subject: {mail_head}\n\n{mail_body}")

