# July 14, 2024

API_KEY = "your_api_key"
MY_LAT = 31.450365
MY_LNG = 73.134964

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "cnt": 4,
    
}

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

import requests
from twilio.rest import Client



account_sid = "your_account_sid"
auth_token = "your_auth_token"

response = requests.get(API_ENDPOINT, params=parameters)

response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["description"])
description = []
IDs = []
ganna_rain = False
for x in range(0, 4):
    description.append(data["list"][x]["weather"][0]["description"])
    IDs.append(data["list"][x]["weather"][0]["id"])
    condition_code = data["list"][x]["weather"][0]["id"]
    if int(condition_code) < 700:
        ganna_rain = True

if ganna_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today",
            from_="+12516517129",
            to="+923120720020"
        )
print(message.status)



