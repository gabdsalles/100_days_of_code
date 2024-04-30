import requests, smtplib, os
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Kindle-Paperwhite-16-GB-adjustable/dp/B09TMN58KL/ref=sr_1_1?crid=2JN1ER6EW49UY&dib=eyJ2IjoiMSJ9.HGf6D6jldta6sEQ0RIMM7D9VbvyqnkwogD30HBB5EycHVTkYqkS5LwBzcNoYjSvsVryzOEN6YoRD7CaqJ6tbMuhOJEivxUVzVyyl6v6FujptG5_swC3S6YsXY6SKWpB54DbSrTCQC-t7a8dxDKr_F8g_BweOgsSm1N-JCfXq8nenNl2pgsvKlgMhC0HE6hOf03HmYDZTm2lXYmsEfue3a4n-r3LULLqutf9RTfRR7cE.08P5dvr9CbXLlJaiuti0fzW3xMrUVRAw7JHlkFopCE0&dib_tag=se&keywords=KINDLE&qid=1714483919&sprefix=kindl%2Caps%2C293&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_float = float(price.split("$")[1])
print(price_float)

target_price = 200

def send_email(price):
    my_email = "gabdsalles@gmail.com"
    my_password = os.environ.get("GOOGLE_PW")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email, 
                            msg=f"Hora de comprar o Kindle! Está na amazon por ${price}".encode('utf-8'))

if price_float < target_price:
    print("Hora de comprar! Mandando e-mail.")
    send_email(price_float)