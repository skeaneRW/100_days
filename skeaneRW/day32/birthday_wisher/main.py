##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
from email.message import EmailMessage
import datetime as dt
from random import choice as randomchoice

from login_info import password
import pandas

df = pandas.read_csv("skeaneRW/day32/birthday_wisher/birthdays.csv")

def get_birthdays(date):
     bdays_df = df[(df.month == 6) & (df.day == 1)]
     bdays_df = bdays_df[["name","email"]]
     return(bdays_df)
     
def get_greeting(name):
    greeting_paths = [
        "skeaneRW/day32/birthday_wisher/letter_templates/letter_1.txt",
        "skeaneRW/day32/birthday_wisher/letter_templates/letter_2.txt",
        "skeaneRW/day32/birthday_wisher/letter_templates/letter_3.txt",
    ]
    path = randomchoice(greeting_paths)
    with open(path, "r") as file:
        content = file.read()
    content = content.replace("Angela","Stephen")
    content = content.replace("[NAME]",name)
    return content

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
'''
now = dt.datetime.now()
if now.strftime("%A") == "Sunday":
        recipient = "aloha.ooze@yahoo.com"
        subject = f"Quote of the Week {now.strftime(f"%A, %B %d")}"
        message = get_random_quote()
        send_email(recipient,subject,message)
'''
birthdays = get_birthdays(dt.datetime.now())
for i in range(len(birthdays)):
    recipient_email = (birthdays.email[i])
    recipient_name = (birthdays.name[i])
    recipient_greeting = get_greeting(recipient_name)
    send_email(recipient_email,"Happy Birthday!",recipient_greeting)


