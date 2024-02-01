#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

sheet_data = dataManager.get_all_rows()

# Popular planilha com IATA codes
# sheet_data = flightSearch.put_iata_code(sheet_data)
# pprint(sheet_data)
# dataManager.edit_iata_code(sheet_data)

# Pesquisar voos mais baratos
for row in sheet_data['prices']:

    flight = flightSearch.find_flights(row['iataCode'])

    if flight.price < row['lowestPrice']:
        notificationManager.send_message(flight)


