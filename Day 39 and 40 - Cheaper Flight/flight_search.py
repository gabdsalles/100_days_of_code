import os
import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from pprint import pprint

KIWI_API_KEY = os.environ.get('KIWI_API_KEY')
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/"
FLY_FROM = "LON"

class FlightSearch:

    def __init__(self):
        self.search_header = {
            "apikey": KIWI_API_KEY
        }
        

    def get_iata_code(self, city):
        
        search_params = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query", params=search_params, headers=self.search_header)
        data = response.json()

        iata = data['locations'][0]['code']
        return iata

    def put_iata_code(self, sheet_data):

        for row in sheet_data['prices']:
            if row['iataCode'] == '':
                row['iataCode'] = self.get_iata_code(row['city'])

        return sheet_data

    def find_flights(self, city_iata):
        
        tomorrow_formatted = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        date_six_months_formatted = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")
        
        search_params = {
            "fly_from": FLY_FROM,
            "fly_to": city_iata,
            "date_from": tomorrow_formatted,
            "date_to": date_six_months_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{KIWI_ENDPOINT}v2/search", params=search_params, headers=self.search_header)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            
            search_params["max_stopovers"] = 1
            response = requests.get(url=f"{KIWI_ENDPOINT}v2/search", params=search_params, headers=self.search_header)
            try:
                data = response.json()["data"][0]
                pprint(data)
            except IndexError:
                print(f"No flights with 1 stopover for {city_iata}")
                return None
            else:

                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data

        else:
            flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data




    