import os, requests

BEARER_TOKEN = os.environ.get('BEARER_SHEETY')
SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')
SHEETY_POST_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightUsers/users"

print("Welcome to Gabriel's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_confirmation = input("Type your email again.\n")

while email != email_confirmation:
    email_confirmation = input("Type your email again.\n")

def send_to_sheet(first_name, last_name, email):

    header_sheety = {
        "Authorization": BEARER_TOKEN
    }

    sheet_inputs = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response_sheety = requests.post(url=SHEETY_POST_ENDPOINT, json=sheet_inputs, headers=header_sheety)
    print("Success! You're in the club.")


send_to_sheet(first_name, last_name, email)