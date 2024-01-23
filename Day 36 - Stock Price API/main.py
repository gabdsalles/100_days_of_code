import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "TESTE"
API_KEY_NEWS = "TESTE"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_closing_prices():
    
    params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK
}
    response = requests.get(STOCK_ENDPOINT, params=params_stock)
    response.raise_for_status()

    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

    diff_percent = difference / float(yesterday_closing_price) * 100
    return diff_percent

#diff_percent = get_closing_prices()

def get_news(diff_percent):
    
    news_params = {
        "apiKey": API_KEY_NEWS,
        "q": COMPANY_NAME,
        "language": "en"
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()

    data = response.json()["articles"]
    top_3_news = data[:3]
    top_3_titles = [news["title"] for news in top_3_news]
    top_3_description = [news["description"] for news in top_3_news]

    send_message_stock(top_3_titles, top_3_description, diff_percent)

def send_message_stock(headlines, descriptions, diff_percent):

    account_sid = 'AC5dfcba8fab3229ae617a7f8795e90eba'
    auth_token = "TESTE"
    client = Client(account_sid, auth_token)

    if diff_percent > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    for i in range(3):

        title = headlines[i]
        description = descriptions[i]

        corpo_mensagem = f"{STOCK}: {up_down}{abs(diff_percent)}\nHeadline: {title}\nBrief: {description}"
        print(corpo_mensagem)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=corpo_mensagem,
        to='whatsapp:+554298748821'
        )

        print(message.status)
        print("Mensagem enviada com sucesso!")

if abs(diff_percent) > 1:
    get_news(diff_percent)


