# june 20, 2024
# loops and stuff


fruits = ["apple", "banana", "Peach"]
for x in fruits:
    print(x)
    

# calculate average
numbers = [1, 2, 3, 4, 5]
sum = 0
n = 0
for x in numbers:
    sum += x
    n += 1
print(sum/n)

# find max
numbers = [1, 2, 3, 4, 5, 10]
max_num = numbers[0]
for x in numbers:
    if x > max_num:
        max_num = x
print(max_num)


# ranges in loops
sum = 0
for n in range(1, 101): # the end range is not included
    sum += n
print(sum)


# sum of even from 2 to 

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x

print(sum) 

sum2 = 0
for x in range(2, 101, 2):
    sum2 += x
    
print(sum2)


# fizzbuzz
for x in range(1, 31):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)



# number of letter, number of symbols, number of numbers in your password
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passString = ''

for x in  range(1, nr_letters + 1):
    char = random.choice(letters)
    passString += char
for x in range(1, nr_numbers+ 1):
    num = random.choice(numbers)
    passString += num
for x in range(1, nr_symbols+1):
    sym = random.choice(symbols)
    passString += sym
print(passString)

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passList = []
for x in  range(1, nr_letters + 1):
    char = random.choice(letters)
    passList += char
for x in range(1, nr_numbers+ 1):
    num = random.choice(numbers)
    passList += num
for x in range(1, nr_symbols+1):
    sym = random.choice(symbols)
    passList += sym
print(passList)
random.shuffle(passList)
print(passList)
passy = ''
for x in passList:
    passy += x

print(passy)
