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
SHEETY_TOKEN = "Bearer ..."
SHEETY_END_POINT_SRCH_FLGHT = "https://api.sheety.co/.../prices"
SHEETY_END_POINT_SEND_MAIL = "https://api.sheety.co/.../mail"
TEQUILA_END_POINT = "https://tequila-api.kiwi.com"
TEQUILA_APIKEY = "..."

my_email = "..."
smtp_setting = "smtp.inbox.ru"
my_password = "..."

sheety_data_flgt = SheetyData(token=SHEETY_TOKEN, api_end_point=SHEETY_END_POINT_SRCH_FLGHT)
retrive_rows = sheety_data_flgt.get_rows()
retrive_rows.raise_for_status()
sheety_data_mail = SheetyData(token=SHEETY_TOKEN, api_end_point=SHEETY_END_POINT_SEND_MAIL)
mail_rows = sheety_data_mail.get_rows()
mail_rows.raise_for_status()
mail_to_list = mail_rows.json()["mail"]
tequila_data = FlightData(end_point=TEQUILA_END_POINT, apikey=TEQUILA_APIKEY)

rows_flight = retrive_rows.json()["prices"]

# for i in range(len(rows)):
#     current_row = rows[i]
#     cit_name = current_row["city"]
#     srch_res_obj = tequila_data.get_iata_city(city_name=cit_name)
#     srch_res_obj.raise_for_status()
#     city_iata = srch_res_obj.json()
#     if  current_row['iataCode'] == "":
#         current_row['iataCode'] = city_iata
#         info = sheety_data.update_row(chng_rw_id=current_row["id"], body_json={"price": current_row})
current_date = dt.date.today().strftime(DATE_FORMAT_STRING)
to_date = (dt.date.today() + relativedelta(months=SRCH_MNTH_IN_FUTURE)).strftime(DATE_FORMAT_STRING)

for i in range(len(rows_flight)):
    current_row = rows_flight[i]
    price_srch = tequila_data.get_flights(
        from_iata=MY_CITY_IATA,
        to_iata=current_row['iataCode'],
        srch_frm_dt=current_date,
        srch_to_dt=to_date,
        nights_in_min=NGHTS_MIN,
        nights_in_max=NGHTS_MAX
    )
    price_srch.raise_for_status()
    try:
        fl_dt = price_srch.json()["data"][0]
    except IndexError:
        continue
    print(f"{current_row['city']}: {fl_dt} eur")
    my_price_trashhold = current_row['lowestPrice']
    if fl_dt["price"] <= my_price_trashhold:
        from_date = dt.date.fromtimestamp(fl_dt['route'][0]['aTimeUTC'])
        to_date = dt.date.fromtimestamp(fl_dt['route'][-1]['aTimeUTC'])
        mail_head = "Low price alert!"
        mail_body = f"Only {fl_dt['price']} euros to fly from {fl_dt['cityFrom']}-{fl_dt['flyFrom']}" \
                    f"to {fl_dt['cityTo']}-{fl_dt['flyTo']}. {fl_dt['nightsInDest']} Nights.\n" \
                    f"from utc {from_date} to {to_date}."
        for j in range(1, len(fl_dt['route']) - 1):
            mail_body += f"\n\nStop over in {fl_dt['route'][j]['cityCodeFrom']}-{fl_dt['route'][j]['cityFrom']}"

        for prsn in mail_to_list:
            with smtplib.SMTP(smtp_setting) as cnnctn:
                cnnctn.starttls()
                cnnctn.login(user=my_email, password=my_password)
                cnnctn.sendmail(from_addr=my_email,
                                to_addrs=prsn['email'],
                                msg=f"Subject: HI {prsn['firstname']} {mail_head}\n\n{mail_body}")
