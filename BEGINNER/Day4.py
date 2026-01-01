# june 20, 2024
# randomization and lists

import random as r
int = r.randint(1, 10)  # 10 is included
print(int)
floaty = r.random()
print(floaty)

# coin toss

import random as r
print("flipping the coin")
n = r.randint(0, 1)
if n == 0:
    print("heads")
else:
    print("tails")

listy2 = ["pumpkin", "water melon"]
listy = ["apple", "banana", "cherry"]
print(listy[0]) # offsetting and addresses

listy.insert(1, "pineapple")    # index based insertion
for i in listy:
    print(i)

listy.extend(listy2)
for i in listy:
    print(i)

print(len(listy))

fruits = ["apple", "banana", "cherry"]
vegetable = ["turnip", "lady finger", "beet root"]
amalgamate = [fruits, vegetable]
for x in amalgamate:
    for y in x:
        print(y)


# coordinate checking and traversal in nested lists
row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
matrix = [row1, row2, row3]

x = input("enter the coordinates, 0 is the start and 2 is the end (eg: 00, 01, 02)").upper()
konsi_list = int(x[0])
konsa_index_listka = int(x[1])

lister = matrix[konsi_list]
lister[konsa_index_listka] = "X"


print(matrix[0])
print(matrix[1])
print(matrix[2])



# rock paper scissor
import random as r
userChoice = int(input(("Enter 1 for rock, 2 for paper, 3 for scissors")))
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
listy = [rock, paper, scissor]
compChoice = r.randint(1, 3)

if userChoice == 1 and compChoice == 2:
    print(f"You chose:\n {rock}")
    print(f"the computer chose: {paper}")
    print("Paper beats rock, Computer wins")
elif userChoice == 1 and compChoice == 3:
    print(f"You chose:\n {rock}")
    print(f"the computer chose: {scissor}")
    print("Rock beats scissors, You win")
elif userChoice == 2 and compChoice == 1:
    print(f"You chose:\n {paper}")
    print(f"the computer chose: {rock}")
    print("Paper beats rock, You win")
elif userChoice == 2 and compChoice == 3:
    print(f"You chose:\n {paper}")
    print(f"the computer chose: {scissor}")
    print("Scissors beats paper, Computer wins")
elif userChoice == 3 and compChoice == 1:
    print(f"You chose:\n {scissor}")
    print(f"the computer chose: {rock}")
    print("Rock beats scissors, Computer wins")
elif userChoice == 3 and compChoice == 2:
    print(f"You chose:\n {scissor}")
    print(f"the computer chose: {paper}")
    print("Scissors beats paper, You win")
else:
    print(f"you chose:\n {listy[userChoice-1]}")
    print(f"the computer chose:\n {listy[compChoice-1]}")
    print("It's a tie")