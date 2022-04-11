import requests
import datetime as dt

API_ID = "nutritionix_api_id"
API_KEY = "nutritionix_api_key"
end_point_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

MY_HEIGHT_CM = 174.5
MY_WEIGHT_KG = 70
MY_AGE = 21
MY_GENDER = "male"

api_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}
query = input("Enter yours today exercise achievements: ")

api_body = {
    "query": query,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT_KG,
    "height_cm": MY_HEIGHT_CM,
    "age": MY_AGE
}
api_res_nutr = requests.post(url=end_point_nutritionix, headers=api_headers, json=api_body)
api_res_nutr.raise_for_status()
nutr_api_result = api_res_nutr.json()["exercises"]
end_point_sheety = "https://api.sheety.co/e442c94048a965ded887c28ccdf2f161/workouts/workouts"

sheety_headers = {
    "Authorization": "Enter if you needed it",
}
for exer in nutr_api_result:
    sheety_json = {
        "workout":
            {
                "date": dt.datetime.today().strftime("%m/%d/%y"),
                "time": dt.datetime.today().strftime("%H:%M"),
                "exercise": exer["user_input"],
                "duration": exer["duration_min"],
                "calories": exer["nf_calories"],
            }
    }

    api_res_sheety = requests.post(url=end_point_sheety, json=sheety_json, headers=sheety_headers)
    api_res_sheety.raise_for_status()
