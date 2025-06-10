import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def change_in_stock(this_stock):
    AV_ENDPOINT = "https://www.alphavantage.co/query"
    AV_Params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": this_stock,
        "apikey": os.environ.get("AV_APIKEY"),
        "outputsize": "compact"
    }
    response = requests.get(AV_ENDPOINT, AV_Params).json()
    stock_activity = [{"date":date,"close":float(stock["4. close"])} for date, stock in response[ "Time Series (Daily)"].items()][0:2]
    last_close = stock_activity[0]["close"]
    prior_close = stock_activity[1]["close"]
    print(last_close, prior_close)
    result = ((last_close / prior_close)-1) * 100
    print(result)
    return round(result, 1)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(COMPANY_NAME):
    NEWS_ENDPOINT="https://newsapi.org/v2/everything"
    News_Params = {
        "apiKey": os.environ.get("NEWS_API_KEY"),
        "q": COMPANY_NAME,
        "language":"en",
        "pageSize":3
    }
    response = requests.get(NEWS_ENDPOINT, News_Params).json()
    headlines = [{"headline":article["title"],"brief":article["description"]} for article in response["articles"]]
    return headlines

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_sms(recipient_phone, body_message):
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    try:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token, http_client=proxy_client)
    except(KeyError):
        client = Client(account_sid, auth_token)
    message = client.messages.create(
    body= body_message,
    from_='+18447936103',
    to=f'+18777804236', #replace recipient phone with fake number bcs of sms regulations.
    )
    print(message.status)

#Optional: Format the SMS message like this: 

stock_movement = change_in_stock(STOCK)
message = ''
if abs(stock_movement) >= 5:
    message += (f"{STOCK}: {'🔻' if stock_movement < 0 else '🔺'}{abs(stock_movement)}%\n")
    for article in get_news(COMPANY_NAME):
        message += (f"Headline: {article["headline"]}\nBrief: {article["brief"]}\n\n")
    send_sms(9785499363, message)
else:
    print(f'stocks for {STOCK} moved by less than 5% ({stock_movement}) no alerts sent.')

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


