# July 11, 2024

import smtplib

# emails and smtp module and datetime
password = "your_password"
my_email = "your_email"




import smtplib

password = "your_password"
my_email = "your_email"

def send_email(message,receiver):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= receiver,
                            msg = f"Subject: Wishing you an AWESOME Happy Birthdayyyy!!!\n\n{message}")



import datetime as dt
import random as rd
import pandas as pd

df = pd.read_csv("bdays.csv")
names = df["name"]
emails = df["email"]
years = df["year"]
months = df["month"]
days = df["day"]



#print(df)

letters = []
choice = rd.randint(1, 3)
with open(f"letter_templates/letter_{choice}.txt") as file:
    letters.append(file.read())
    #print(letters)
    letter = "".join(letters)


class People:
    def __init__(self, name, email, year, month, day):
        self.name = name
        self.email = email
        self.year = year
        self.month = month
        self.day = day
        self.dob = dt.datetime(year=self.year, month=self.month, day=self.day)

people = []
for i in range(0, 3):
    r = People(names[i], emails[i], years[i], months[i], days[i])
    people.append(r)


currentDate = dt.datetime.now()
currentMonth = currentDate.month
currentDay = currentDate.day


for x in people:
    if currentMonth == x.dob.month and currentDay == x.dob.day:
        customLetter = letter.replace("[NAME]",x.name)
        customLetter = customLetter.replace("Angela", "Syed Junaid Jaffery")
        send_email(customLetter, x.email)
        print("Message sent successfully!")
