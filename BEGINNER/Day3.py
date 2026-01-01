# june 15, 2024

# conditional statements
n = 1
if n < 0:
    print("the if condition was met")
else:
    print("the else condition was met")


# basic if elif and else statements


# bmi calculator
height = float(input("what is your height in meters"))
weight = int(input("what is your weight in kg"))
bmi = weight / (height**2)
if bmi < 18.5:
    print("you are underweight")
elif bmi < 23:
    print("you are normal weight")
elif bmi < 27.5:
    print("you are overweight")
else:
    print("you are obese")


# is it a leap year
year = int(input("what year would you like to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")



# pizza bill
size = input("enter S for small, M for medium and L for large")
add_pepperoni = input("press Y to add pepperoni or N to not add it")
extra_cheese = input("Press Y to add extra cheese or N to not")

bill = 0
if size == 'S':
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25
if (size == 'L' or size == 'M') and add_pepperoni == 'Y':
    bill += 3
if extra_cheese == 'Y':
    bill += 1
print(f"the final bill is {bill}")



# love calculator
name1 = input("enter your name").upper()
name2 = input("enter your partner's name").upper()
name1 = name1
num1 = 0
num2 = 0

for s in name1:
    if s == 'T' or s == 'R' or s == 'U' or s == 'E':
        num1 += 1
    if s == 'L' or s == 'O' or s == 'V' or s == 'E':
        num2 += 1
for s in name2:
    if s == 'T' or s == 'R' or s == 'U' or s == 'E':
        num1 += 1
    if s == 'L' or s == 'O' or s == 'V' or s == 'E':
        num2 += 1
print(num1, num2)

num1 *= 10
lovescore = num1+num2
if lovescore < 10 or lovescore > 90:
    print(f"your score is {lovescore}, you go together like coke and mentos")
elif lovescore >= 40 and lovescore <= 50:
    print(f"your score is {lovescore}, you are alright together")
else:
    print(f"your score is {lovescore}")




# remember ascii art, might be useful in uni

