import os
import requests
from pprint import pprint

SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
BEARER_TOKEN = os.environ.get('BEARER_SHEETY')
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}"

class DataManager:
    
    def __init__(self):

        self.header_sheety = {
            "Authorization": BEARER_TOKEN
        }

    def get_all_rows(self):

        response = requests.get(url=f"{SHEETY_ENDPOINT}/flightDeals/prices", headers=self.header_sheety)
        data = response.json()
        #pprint(data)
        return data

    def edit_iata_code(self, sheet_data):

        for row in sheet_data['prices']:
            
            row_id = row['id']

            sheet_inputs = {
                "price": {
                    "city": row['city'],
                    "iataCode": row['iataCode'],
                    "lowestPrice": row['lowestPrice']
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=sheet_inputs, headers=self.header_sheety)
            #print(response)

    def get_all_users(self):

        response = requests.get(url=f"{SHEETY_ENDPOINT}/flightUsers/users", headers=self.header_sheety)
        data = response.json()
        #pprint(data)
        return data


            


    