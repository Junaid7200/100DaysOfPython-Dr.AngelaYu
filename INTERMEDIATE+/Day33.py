# July 12, 2024


MY_LAT = 31.411930
MY_LNG = 73.108050
# application programming interfaces
# me-->menu-->restaurant analogy
# api endpoints: a location the data is stored kinda, like api.coinbase.com
# api calls: the request to the data

# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# response codes, if it starts with 1, it means hold on, something is happening. if its 2 something then its final and its done, it just means here you go. if its 3 something then you don't have the permission or authorization for the thing you are trying to access. if its 4 something then it means you screwed up or the thing doesn't exist. if its 5 something then the server screwed up

# api parameters
import requests
import datetime as dt
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": "Asia/Karachi",
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
#print(data)
sunrise = data["results"]["sunrise"]
#print(sunrise)
sunset = data["results"]["sunset"]
#print(sunset)

currentTime = dt.datetime.now()

sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
print(sunrise_hour)
sunset_hour = int(sunset.split("T")[1].split(":")[0])
print(sunset_hour)
current_hour = currentTime.hour
print(current_hour)

ISS_location = requests.get(url="http://api.open-notify.org/iss-now.json")
ISS_location.raise_for_status()

data = ISS_location.json()
print(data)
ISS_longitude = float(data["iss_position"]["longitude"])
ISS_latitude = float(data["iss_position"]["latitude"])
ISS_position = (ISS_longitude, ISS_latitude)

import time
while True:
    time.sleep(60)
    if MY_LAT-5 <= ISS_latitude <= MY_LAT+5 and MY_LNG-5 <= ISS_longitude <= MY_LNG+5:
        if current_hour >= sunset or current_hour <= sunrise_hour:
            import email_sender as es
            es.send_email("The International Space Station is over your head!!!", "bleh")