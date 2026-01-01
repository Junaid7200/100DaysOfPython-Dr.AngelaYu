# june 13, 2024
# Day 2 of 100 days of python
# data types, f strings, 


# day 2 project attempt with no prep
print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? (10, 12 or 15% of the total bill)\n"))
if tip == 10:
    tipAmount = totalBill * 0.1
elif tip == 12:
    tipAmount = totalBill * 0.12
elif tip == 15:
    tipAmount = totalBill * 0.15
else:
    tipAmount = 0

totalBill += tipAmount
people = float(input("How many people to split the bill\n"))
eachPerson = float(totalBill/people)
print(f"Each person should pay: {"{:.2f}".format(eachPerson)}")


#
# SUCCESS

# data types
"hello"[-1]  # thats called sub scripting
n = 1_000_000   # you can use under score in int values in python to make it more readable
x = 4_3_4
print(n+x)

# ints and float and boolean, nothing interesting
# type errors and type conversions and type checking

type(120)
type("string")
n = "123"
int(n)


# add a two digit number
n = input("Enter a two digit number: ")
num1 = n[0]
num2 = n[1]
sum = int(num1) + int(num2)
print(sum)

# sub, mul, div, exponentiation
# pemdas and order of execution of operations

height = float(input("enter your height in kg"))
weight = float(input("enter your weight in cm"))
BMI = weight / height ** 2
print(BMI)

# number manipulation
print(round(8/3))
print(8//3) # floor division

# 4000 weeks
age = int(input("enter your age"))
No_of_years_left = 90 - age
No_of_days_left = No_of_years_left * 365
No_of_weeks_left = No_of_days_left / 7
print(f"You have {No_of_days_left} days, {No_of_weeks_left} weeks left")

