import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
from config import password
from time import sleep

MY_LAT = 42.523086726091414 # Your latitude
MY_LONG = -71.7644583171791 # Your longitude

def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    latitude_diff = iss_latitude - MY_LAT
    longitude_diff = iss_longitude - MY_LONG
    return (abs(latitude_diff) <= 5) and (abs(longitude_diff) <= 5)


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    utc_diff = 4
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + utc_diff
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + utc_diff

    time_now = datetime.now()
    current_hour = time_now.hour
    return current_hour >= sunset or current_hour <= sunrise

def send_email(msg_to, msg_subject, msg_content,):
    my_email = "aloha.ooze@gmail.com"
    gmail_host = "smtp.gmail.com"
    with smtplib.SMTP(gmail_host, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        msg = EmailMessage()
        msg.set_content(msg_content)
        msg["Subject"] = msg_subject
        msg["From"] = my_email
        msg["To"] = msg_to
        connection.send_message(msg)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    sleep(60)
    if is_dark() and iss_nearby():
        send_email("stephenakeane@gmail.com", "ISS Locator", "the ISS is nearby!")
    






