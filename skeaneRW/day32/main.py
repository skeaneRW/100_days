import smtplib
import datetime as dt
from email.message import EmailMessage
from login_info import password


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

# send_email("aloha.ooze@yahoo.com", "Dinner Plans?","I'm hungry. Lets get sushi!")

now = dt.datetime.now()
formatted_date = now.strftime("%m/%d/%Y")
def format_date(date):
    return date.strftime("%m/%d/%Y")
dob = dt.datetime(year=1974, month=9, day=25)

print(formatted_date, format_date(dob))