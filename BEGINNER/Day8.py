# # June 26, 2024
# # caesar cipher program
# # functions with inputs

# # default args after non default
# def greet(designation, name = "Naam"):
#     print("Hello!")
#     print(f"How are you doing today {name}?")
#     print(f"How's life as a {designation}?")


# # keyword arguments is when you write the parameter and then the args
# greet(name = "James", designation = "Data Scientist")


# # how many cans of paint do i need
# import math # for ceil and floor
# def calcCans(height, width, coverage):
#     NoOfCans = (height * width) / coverage
#     return NoOfCans

# math.ceil(calcCans(3, 9, 5))


# # prime numbers, div by themselves and 1

# def isPrime(n):
#     for x in range(1, n):
#         if n % x == 0 and x != 1 and x != n:
#             return False
#     return True


# print(isPrime(1))
# print(isPrime(3))
# print(isPrime(5))
# print(isPrime(4))
# print(isPrime(8))
# print(isPrime(21))


# # caesar cipher part 1

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char) % 26
            new_position = (position + shift) % 26
            if (new_position > 25):
                new_position = (new_position - 26) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The encoded text is {cipher_text}")

encrypt("civilization", 5)


def decrypt(text, shift):
    plain_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char) % 26
            new_position = (position - shift) % 26
            if (new_position < 0):
                new_position = (new_position + 26) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The decoded text is {plain_text}")

decrypt("hnanqnefynts", 5)




logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""



def direct(choice):
    if choice == "encode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif choice == "decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Invalid choice. Please choose 'encode' or 'decode'")

check = 1
while(check == 1):
    print(logo)
    check = int(input("Press 1 to start and 0 to exit"))
    if check == 1:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        direct(direction)
    else:
        print("Exiting the program")

