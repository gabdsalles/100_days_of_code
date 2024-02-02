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
users_data = dataManager.get_all_users()

# Popular planilha com IATA codes
# sheet_data = flightSearch.put_iata_code(sheet_data)
# pprint(sheet_data)
# dataManager.edit_iata_code(sheet_data)

# Pesquisar voos mais baratos
for row in sheet_data['prices']:

    flight = flightSearch.find_flights(row['iataCode'])

    try:
        if flight.price < row['lowestPrice']:
            message_body = f'Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.'
            if flight.stop_overs > 0:
                message_body = message_body + f"Flight has {flight.stop_overs} stop over, via {flight.via_city}."
            
            #notificationManager.send_message(message_body)
            users_data = dataManager.get_all_users()
            for user in users_data['users']:
                notificationManager.send_emails(user['email'], message_body)

    except AttributeError:
        print(f"No flights found for {row['city']}.")
    finally:
        continue


