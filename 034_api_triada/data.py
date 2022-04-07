import requests

Q_AMOUNT = 10
Q_TYPE = "boolean"
Q_END_POINT = "https://opentdb.com/api.php"
parameters = {
    "amount": Q_AMOUNT,
    "type": Q_TYPE
}


data_from_api = requests.get(url=Q_END_POINT, params=parameters)
data_from_api.raise_for_status()
question_data = data_from_api.json()["results"]
