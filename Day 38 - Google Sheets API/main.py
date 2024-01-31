import requests
import os
from datetime import datetime


APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
BEARER_TOKEN = os.environ.get('BEARER_SHEETY')
SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "180"
AGE = "21"


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": input("Me diga quais exercícios você fez hoje? "),
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=header)
result = response.json()
print(result)

SHEETY_POST_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/myWorkouts/workouts"

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

header_sheety = {
    "Authorization": BEARER_TOKEN
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response_sheety = requests.post(url=SHEETY_POST_ENDPOINT, json=sheet_inputs, headers=header_sheety)
    print(response_sheety)
