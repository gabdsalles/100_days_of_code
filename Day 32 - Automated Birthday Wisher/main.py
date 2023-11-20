import pandas as pd
import datetime as dt
import smtplib
import random

def generate_message(name):

    number = random.randint(1, 3)
    with open(f"./Day 32 - Automated Birthday Wisher/letter_templates/letter_{number}.txt") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", name)

    return letter_content

def send_email(email_dest, birthday_message):
    my_email = "gabdsalles@gmail.com"
    my_password = "TESTE"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_dest, 
                            msg=f"Subject: Happy Birthday!\n\n{birthday_message}")


birthdays = pd.read_csv("./Day 32 - Automated Birthday Wisher/birthdays.csv")
birthdays = birthdays.to_dict(orient="records")

now = dt.datetime.now()
today = (now.day, now.month)

for birthday in birthdays:

    birthday_day = (birthday["day"], birthday["month"])

    if today == birthday_day:
        
        birthday_message = generate_message(birthday["name"])
        send_email(birthday["email"], birthday_message)