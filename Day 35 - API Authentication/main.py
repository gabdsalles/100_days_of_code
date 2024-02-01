import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
lat = "-25.0945"
long = "-50.1633"

parameters = {
    "appid": api_key,
    "lat": lat,
    "lon": long,
    "cnt": 4
}

def send_message():
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Vai chover! Leve um ☂️',
    to='whatsapp:+554298748821'
    )

    print(message.status)
    print("Mensagem enviada com sucesso!")

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()

print(response.status_code)

weather_data = response.json()

will_rain = False

for i in range(4):

    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    send_message()
else:
    print("Não vai chover.")

