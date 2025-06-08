import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_params = {
    "lat": 42.525860,
    "lon": -71.760132,
    "appid": os.environ.get("OWM_API_KEY"),
    "cnt": 4
}
response = requests.get(OWM_endpoint, params=OWM_params)
response.raise_for_status()
weather_data = response.json()

def will_rain() -> bool:
    rain_in_forecast = [True if hourly_forecast["weather"][0]["id"] < 799 else False for hourly_forecast in weather_data["list"]]
    return any(rain_in_forecast)

def send_sms(recipient_phone):
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid='HXc6b1e52fc48028d4574fc9b881c11e87',
    content_variables='{"1":"12/1","2":"3pm"}',
    to=f'whatsapp:+1{recipient_phone}'
    )
    print(message.status)

def run_rain_checker():
    print('checking for rain...')
    if will_rain():
        print('rain in forecast')
        send_sms(9785499363)
    else:
        print('clear skies, will check again tomorrow')

run_rain_checker()

