from random import randint
import smtplib
import datetime as dt
from email.message import EmailMessage
from login_info import password


def get_random_quote():
    with open("skeaneRW/day32/quote_of_the_week/quotes.txt") as file:
        quote_list = [line.strip() for line in file.readlines()]
    return quote_list[randint(0, len(quote_list)-1)]

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

now = dt.datetime.now()
if now.strftime("%A") == "Sunday":
        recipient = "aloha.ooze@yahoo.com"
        subject = f"Quote of the Week {now.strftime(f"%A, %B %d")}"
        message = get_random_quote()
        send_email(recipient,subject,message)
        