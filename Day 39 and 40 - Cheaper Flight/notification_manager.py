import os
import smtplib
from twilio.rest import Client

class NotificationManager:
    
    def __init__(self):
        pass

    def send_message(self, m_body):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=m_body,
        to='whatsapp:+554298748821'
        )

        print(message.status)
        print("Mensagem enviada com sucesso!")

    def send_emails(self, email, m_body):
        my_email = "gabdsalles@gmail.com"
        my_password = os.environ.get("GOOGLE_PW")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            try:
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=m_body.encode('utf-8'))
                print("Email sent successfully!")
            except Exception as e:
                print(f"An error occurred: {str(e)}")