# July 11, 2024

import smtplib

# emails and smtp module and datetime
password = "your_password"
my_email = "your_email"



# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs= "junaidjaffery1@hotmail.com", 
#                         msg = "Subject: This is the subject\n\nyoyo what up dawg, this is the body of the email btw")

import random as rd

def send_email(receiver):
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = rd.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= receiver,
                            msg = f"Subject: Hey there\n\n{quote}")


import datetime as dt

# currentDate = dt.datetime.now()
# weekday = currentDate.weekday()
# print(currentDate)
# print(currentDate.year)


dob = dt.datetime(year=2004, month=11, day=30)
print(dob)


currentDate = dt.datetime.now()
weekday = currentDate.weekday()

if weekday == 0:
    send_email(receiver="receiver_mail")
if weekday == 0:
    send_email(receiver="receiver_mail")
    send_email(receiver="receiver_mail")