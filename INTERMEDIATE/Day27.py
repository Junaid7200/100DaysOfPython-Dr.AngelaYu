# July 6, 2024

#! left at 004, start from 005 when you see this

# from tkinter import *

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# #Buttons
# def action():
#     print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()





















# from tkinter import *

# from numpy import pad

# window = Tk()
# window.title("This is a window")
# window.minsize(width=500, height=300)
# window.config(padx=50, pady=50)
# # label

# my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
# my_label.grid(column=0, row=0)

# def button_clicked():
#     my_label["text"] = input.get()

# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1, row=1)

# button2 = Button(text="Click me as well")
# button2.grid(column=2, row=0)
# # entry
# input = Entry(width=10)
# x = input.get()
# input.grid(column=3, row=2)

# default args: you already know this
# unlimited positional args using *

# def add (*args):    # args is a tuple
#     sum = 0
#     for arg in args:
#         sum += arg 
#     print(sum)
# add(1,2,3,4,5,6)


# # unlimited keyword args using **
# def calculate(n, **kwargs): # kwargs is not a tuple, its a
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add = 3, multiply = 5)




from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input_miles.get()
    km = float(new_text) * 1.609
    km_calc["text"] = f"{km}"


window = Tk()
window.title("Miles to km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Labels
equals_label = Label(text="is equal to: ", font=("Arial", 24, "bold"))
equals_label.grid(column=0, row=1)

miles_label = Label(text = "Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

Km_label = Label(text = "Km", font=("Arial", 24, "bold"))
Km_label.grid(column=2, row=1)

km_calc = Label(text= "0", font=("Arial", 24, "bold"))
km_calc.grid(column=1, row= 1)
#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input_miles = Entry(width=10)
print(input_miles.get())
input_miles.grid(column=1, row=0)









window.mainloop()


window.mainloop()