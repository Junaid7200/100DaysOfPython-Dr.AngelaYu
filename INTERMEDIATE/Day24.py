# July 6, 2024

# modifications in snake

# with open("INTERMEDIATE/my_file.txt") as file:
#     contents = file.read()
#     print(contents)




# mail merge
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("INTERMEDIATE/Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    print(contents)

with open("INTERMEDIATE/Input/Names/invited_names.txt") as file:
    names = []
    for name in file.readlines():
        names.append(name.strip())


readied_msgs = []
for name in names:
    msg = contents.replace("[name]", name)
    readied_msgs.append(msg)
    with open(f"INTERMEDIATE/Output/ReadyToSend/letter_for_{name}.txt", mode = "w") as file:
        file.write(msg)
    



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp