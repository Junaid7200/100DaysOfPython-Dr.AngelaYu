# June 29, 2024
# CAPSTONE NO. 1

# black jack: getting as close to 21 as possible: queen jack etc are all 10
# if you go over 21, the dealer wins

# if you go over 21, its a bust, you lose instantly. the ace can be a 1 or an 11
# draw condition, if a dealer has less then 17, he must take another card



############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""


import random as r
import os

def RandPicker(cards, dec):
    dealerChoice = r.randint(0, len(cards) - 1)
    pick = cards[dealerChoice]
    if pick == 11:
        if sum(dec) + pick > 21:
            pick = 1
        dec.append(pick)
        return dec
    else:
        dec.append(cards[dealerChoice])
        return dec


def dealersChoice(dec, cards):
    while sum(dec) < 17:
        dec = RandPicker(cards, dec)
    else:
        pass

def WinnerCheck(userDec, dealerDec):
    if sum(userDec) > 21:
        print(f"You Lose. Your score was {sum(userDec)}; The dealer's score was {sum(dealerDec)}")
        print(f"Your final hand was {userDec}; The dealer's final hand was {dealerDec}")
    elif sum(dealerDec) > 21:
        print(f"You Win. Your score was {sum(userDec)}; The dealer's score was {sum(dealerDec)}")
        print(f"Your final hand was {userDec}; The dealer's final hand was {dealerDec}")
    elif sum(userDec) == sum(dealerDec):
        print(f"Draw. Your score was {sum(userDec)}; The dealer's score was {sum(dealerDec)}")
        print(f"Your final hand was {userDec}; The dealer's final hand was {dealerDec}")
    elif sum(userDec) > sum(dealerDec):
        print(f"You Win. Your score was {sum(userDec)}; The dealer's score was {sum(dealerDec)}")
        print(f"Your final hand was {userDec}; The dealer's final hand was {dealerDec}")
    else:
        print(f"You Lose. Your score was {sum(userDec)}; The dealer's score was {sum(dealerDec)}")
        print(f"Your final hand was {userDec}; The dealer's final hand was {dealerDec}")

def StartState():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    userDec = []
    dealerDec = []
    userDec = RandPicker(cards, userDec)
    userDec = RandPicker(cards, userDec)
    dealerDec = RandPicker(cards, dealerDec)
    dealerDec = RandPicker(cards, dealerDec)
    return cards, userDec, dealerDec


def Game():
    cards, userDec, dealerDec = StartState()
    print(f"Your Cards: {userDec}, currentScore: {sum(userDec)}")
    print(f"The Dealer's first card: {dealerDec[0]}")
    if sum(userDec) == 21:
        print("You Win, you started off with a BlackJack")
        return
    elif sum(dealerDec) == 21:
        print("You lose, dealer started off with a BlackJack")
        return
    elif sum(userDec) == 21 and sum(dealerDec) == 21:
        print("Draw, both you and the dealer started off with a BlackJack")
        return
    else:
        dealersChoice(dealerDec, cards)
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        while choice == 'y':
            if sum(userDec) > 21:
                print("You Lose, you went over 21")
                print(f"The dealer's final hand was: {dealerDec}")
                return
            if choice == 'y':
                userDec = RandPicker(cards, userDec)
                print(f"Your Cards: {userDec}, currentScore: {sum(userDec)}")
                print(f"The Dealer's first card: {dealerDec[0]}")
                if sum(userDec) > 21:
                    print("You Lose, you went over 21")
                    print(f"The dealer's final hand was: {dealerDec}")
                    return
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
            elif choice == 'n':
                WinnerCheck(userDec, dealerDec)
                return
        else:
            WinnerCheck(userDec, dealerDec)
            return



while True:
    choice1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice1 == 'n':
        print("Goodbye!")
        break
    elif choice1 == 'y':
        os.system("cls")
        print(logo)
        Game()


