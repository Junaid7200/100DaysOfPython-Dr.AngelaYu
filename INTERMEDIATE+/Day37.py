# July 16, 2024

# post put and delete requests

import requests

USERNAME = "your_username"
TOKEN = "your_token"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading",
    "unit": "Pages Read",
    "type": "int",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}

# https://pixe.la/v1/users/junaid456/graphs/graph1

# response = requests.post(url =graph_endpoint, json = graph_config, headers=headers )
# print(response.text)

import datetime as dt

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


today = dt.datetime.now()
print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

# response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers= headers)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20240716"


new_pixel_data = {
    "quantity": "25"
}

# response = requests.put(url = update_endpoint, json = new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20240716"

# response = requests.delete(url = delete_endpoint, headers=headers)
# print(response.text)