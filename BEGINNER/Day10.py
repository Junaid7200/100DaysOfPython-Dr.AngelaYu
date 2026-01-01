# # June 26, 2024
# # functions with outputs

# def format_name(first, last):
#     formatted_first = first.title()
#     formatted_last = last.title()
#     return f"{formatted_first} {formatted_last}"

# print(format_name("junaid", "jaffery"))

# # next part of the course
# # functions with multiple returns
# def format_name2(first, last):
#     if not first or not last:
#         return "You didn't provide valid inputs."
#     formatted_first = first.title()
#     formatted_last = last.title()
#     return f"{formatted_first} {formatted_last}"

# # next
# print(format_name2("junaid", "jaffery"))

# # next part of the course
# # functions with multiple returns
# def format_name3(first, last):
#     if not first or not last:
#         return "You didn't provide valid inputs.", False
#     formatted_first = first.title()
#     formatted_last = last.title()
#     return f"{formatted_first} {formatted_last}", True

# # next
# result, success = format_name3("junaid", "jaffery")

# # next part of the course
# # functions with multiple returns
# if success:
#     print(result)
# else:
#     print("Error: " + result)

# # next part of the course
# # functions with multiple returns
# def format_name4(first, last):
#     if not first or not last:
#         return {"status": "failed", "reason": "You didn't provide valid inputs."}
#     formatted_first = first.title()
#     formatted_last = last.title()
#     return {"status": "success", "full_name": f"{formatted_first} {formatted_last}"}

# format_name4("Junaid", "Jaffery")


# def isLeap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False




# doc strings in python
# what is a doc string
# a doc string is a string literal that occurs as the first statement in a module, function,
# class, or method definition. It is used to document the function, class, or module.
# it is used to provide a description of what the function does, what parameters it takes, and
# what it returns.

# calculator

logo = """
 _____________________
|  _________________  |
| | Python   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system("cls")
      calculator()

calculator()
