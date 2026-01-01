# # June 26, 2024
# # dictionaries and nesting

# # silent auction program

# # dictionaries
# # whats a key and whats a value?

# programming_dictionary = {
#  "Bug": "An error in a program that prevents the program from running as expected.",
#  "Function": "A piece of code that you can easily call over and over again.",
#  "Loop": "The action of doing something over and over again",
#  123: "one, two, three ma dude",
#  }

# programming_dictionary[123]   # enter the key and get the value

# programming_dictionary["OOP"] = "Object Oriented Programming"   # adding key value pair

# programming_dictionary["OOP"]

# print(programming_dictionary)

# # programming_dictionary = {} # the dict is now empty

# programming_dictionary[123] = "yo ma dude"  # edit a key value pair

# print(programming_dictionary[123])

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# # printing  dictionary using for loop:
# for key, value in programming_dictionary.items():
#     print(f"{key}: {value}")


# # student scores
# student_scores = {
#  "Harry": 81,
#  "Ron": 78,
#  "Hermione": 99,
#  "Draco": 74,
#  "Neville": 62
# }

# # ignore the error below
# for key, value in student_scores.items():
#     if value >= 91 and value <= 100:
#         student_scores[key] = "Outstanding"
#     elif value >= 81 and value <= 90:
#         student_scores[key] = "Exceeds Expectations"
#     elif value >= 71 and value <= 80:
#         student_scores[key] = "Acceptable"
#     else:
#         student_scores[key] = "Fail"


# for key, value in student_scores.items():
#     print(f"{key}: {value}")



# travel_log = [
#  {"Country": "France",
#  "Cities_Visited": ["Paris", "Lille", "Dijon"],
#  "NoOfVisits": 12},

#  {"Country": "Germany",
#  "Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"],
#  "NoOfVisits": 8},
# ]

# for x in travel_log:
#     print(x)



# # add to the list
# def addCountry(country, cities_visited, visits):
#     new_dict = {
#      "Country": country,
#      "Cities_Visited": cities_visited,
#      "NoOfVisits": visits}
#     travel_log.append(new_dict)

# travel_log = [
#  {"Country": "France",
#  "Cities_Visited": ["Paris", "Lille", "Dijon"],
#  "NoOfVisits": 12},
#  {"Country": "Germany",
#  "Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"],
#  "NoOfVisits": 8},
# ]

# country = input("enter a country\n")
# cities_visited = eval(input("Enter the list of cities visited\n"))
# visits = int(input("enter the number of times you visited this country\n"))
# addCountry(country, cities_visited, visits)



# for x in travel_log:
#     print(x)

import os

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Display logo
logo = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Function to get valid integer input
def get_valid_bid(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main auction logic
def secret_auction():
    bidders = []
    continue_bidding = True

    while continue_bidding:
        print(logo)
        name = input("Enter your name: ")
        bid = get_valid_bid("Enter your bid: $")
        bidders.append({name: bid})

        cont = input("Do you want to continue bidding? (yes/no): ").strip().lower()
        if cont == "no":
            continue_bidding = False
        elif cont != "yes":
            print("Invalid input. Assuming you want to continue.")
        
        clear_screen()

    # Find the highest bidder
    highest_bid = 0
    winner = ""

    for bidder in bidders:
        for name, bid in bidder.items():
            if bid > highest_bid:
                highest_bid = bid
                winner = name

    clear_screen()
    print(logo)
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}.")

# Run the auction
secret_auction()
