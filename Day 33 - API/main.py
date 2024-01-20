import smtplib
import time
import requests
from datetime import datetime

MY_LAT = -25.069630
MY_LNG = -50.149230

response = requests.get("http://api.open-notify.org/iss-now.json")

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (latitude, longitude)

parametros = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parametros)
response.raise_for_status()

data = response.json()
nascer_do_sol = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
por_do_sol = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(f"Posição atual da ISS: {iss_position}")
print(f"Minha posição: ({MY_LAT}, {MY_LNG})")

def send_email():
    my_email = "gabdsalles@gmail.com"
    my_password = "TESTE"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gabteste29@gmail.com", 
                            msg="Olhe pra cima! A ISS ta passando perto de voce agora.")

while True:
    time.sleep(60)
    
    if abs(latitude - MY_LAT) < 5 and abs (longitude - MY_LNG) < 5 and (time_now.hour > por_do_sol or time_now.hour < nascer_do_sol):
        print("A ISS está perto")
        send_email()
    else:
        print("A ISS está longe de você.")