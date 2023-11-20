import datetime as dt
import smtplib
import random

def get_quote():
    with open("./Day 32 - SMTP/quotes.txt") as file:
        
        quotes_list = []
        lines = file.readlines()
        return random.choice(lines)

def send_email(quote):
    my_email = "gabdsalles@gmail.com"
    my_password = "TESTE"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gabteste29@gmail.com", 
                            msg=f"Subject: Quote of the day\n\n{quote}")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:

    quote = get_quote()
    send_email(quote)