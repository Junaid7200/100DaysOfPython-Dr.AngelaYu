# July 6, 2024

# list comprehensions

# format:   new_list = [new_item for item in list]
list = [1, 2, 3]
new_list = [item+1 for item in list]
print(new_list)

# strings:
name = "Junaid"
new_list = [n for n in name]
print(new_list)

double_list = [x*2 for x in range(1, 5)]
print(double_list)

# conditioned list comprehension

# format: new_list = [new_item for item in list if condition]

even_numbers = [p for p in range(1, 10) if p%2 == 0 ]
print(even_numbers)


squared_numbers =  [n*n for n in range(1, 11)]
print(squared_numbers)


# dictionary comprehension:

# format: new_dict = {new_key:new_value for item in list}
# format: new_dict = {new_key:new_value for (key, value) in dict.items()}

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
import random
rand_dict = {name: random.randint(10,50) for name in names}
print(rand_dict)

passed_std = {name:marks for name, marks in rand_dict.items() if marks > 30}
print(passed_std)


sentence = "do what other people aren't willing to do today. So, tomorrow you get to do what others can't"
words = sentence.split()    # split according to white space

word_dict = {word:len(word) for word in words}
print(word_dict)



# pandas data frame comprehension

import pandas as pd 
df = pd.read_csv("INTERMEDIATE/weather-data.csv")
# looping through the rows of the data frame

for (index, row) in df.iterrows():
    print(row.temp)



# nato phonetic alphabets:

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}


df = pd.read_csv("INTERMEDIATE/nato_phonetic_alphabet.csv")
phonetics_dict = {row.letter: row.code for index, row in df.iterrows()}
print(phonetics_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


word = input("Enter a word that only contains alphabets: ").upper()

code = [phonetics_dict[letter] for letter in word if letter in phonetics_dict]
print(code)