# june 13, 2024
# day 1 is mostly introduction so far. that code book is really cool i think
# cornell method
# printing, commenting, string manipulation, errors
# you can check the project of each day using the link in the folder


n = "junaid"
print("hello " + n)

listy = ["Junaid", "Hasnain", "Rehan", "Salman"]

for x in listy:
    x = x + " ma bro"
    print("Hello " + x)


# test 1
print("1. Mix 500g of Flour, 1-g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes")

# test 2, escape sequence
print("She said \"hello\"")

# \n, nothing interesting
print("hello there you little monkey\nhow are you")


# string concatenation
print("hello there" + " you little rabbit") 

# indentation matters mate

# test 2, debug the code
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print("e.g. print(\"Hello\" + \"world\")")
print("New lines can be created with a backslash and n.")

# input function
print("Hello " + input("What is your name\n"))

# test 3, inputs
n1 = int(input("enter a number"))
n2 = int(input("enter another number"))
print(n1 ** n2) # double * for exponentiation

str1 = input("enter a string")
print(len(str1))


print(len(input("enter a string here to see its length")))



# variables, its all really basic
# test 4
a = 15
b = 20

print("Original numbers")
print("a:", a)
print("b:", b)

print("Swapped values")
temp = a
a = b
b = temp
print("a:", a)
print("b:", b)



# variable naming conventions, basic stuff, nothing interesting



# Day 1 project; this is just too simple, hangman was much cooler
print("Welcome to the Band Name Generator.")
city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name is " + city + " " + pet)


# DAY 1 COMPLETED