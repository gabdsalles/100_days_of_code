import os
from twilio.rest import Client

class NotificationManager:
    
    def __init__(self):
        pass

    def send_message(self, flight):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.',
        to='whatsapp:+554298748821'
        )

        print(message.status)
        print("Mensagem enviada com sucesso!")