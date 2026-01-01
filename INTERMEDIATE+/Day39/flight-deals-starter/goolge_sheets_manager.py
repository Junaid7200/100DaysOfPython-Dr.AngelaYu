SHEETY_GET_URL = "https://api.sheety.co/YOUR_SHEETY_ID/copyOfFlightDeals2/prices"
SHEETY_POST_URL = "https://api.sheety.co/YOUR_SHEETY_ID/copyOfFlightDeals2/prices"
SHEETY_PUT_URL = "https://api.sheety.co/YOUR_SHEETY_ID/copyOfFlightDeals2/prices"




class TransactionsSheet:
    def __init__(self):
        pass

    def insert_transaction(self):   # take input of desc, amount, category and type from the user. just these 4 things
        pass

    def fill_values(self):   # get the 4 things from insert_transaction, and calc the date, converted amount and remaining budget columns. get that perfect row
    #data from the budget sheet and the currency converter class both will be needed for this
        pass

    def insert_to_sheet(self):  # get all the inputs from the fill_values method and then insert that as a row into the transactions sheet using an API
        pass
    












class BudgetSheet:
    pass










































































































# from regex import F
# import requests

# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     def __init__(self):
#         self.destination_data = {}
#         self.sheety_data = {}
#         self.sheety_data = self.get_destination_data()
#         print(self.sheety_data)
#         #self.destination_data = self.get_destination_data()
    
#     def get_destination_data(self):
#         response = requests.get(url=SHEETY_GET_URL)
#         data = response.json()
#         self.sheety_data = data
#         return self.sheety_data
#     def update_sheets_data(self):
#         for x in range (2, 10):
            
#             put_url = f"{SHEETY_PUT_URL}/{x}"
#             body = {
#                 "price": {
#                     "iataCode": "TESTING"
#                 }
#             }
#             response = requests.put(url= put_url, json= body)
#             print(response.text)
        
#         # for rows in self.sheety_data:
#         #     rows["iataCode"] = "Testing"
#         # print("After updates: ", self.sheety_data)