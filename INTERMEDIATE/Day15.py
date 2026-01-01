# July 1, 2024

# coffee machine, 3 flavors, diff price, diff ingredients, coin operated. print reports. 

#from tkinter import Menu


MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

print(f"{MENU['espresso']['ingredients']['coffee']}")
print(f"{MENU["espresso"]["cost"]}")



resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def Show_prompt():
    typeOfCoffee = input("What would you like? (espresso/latte/cappuccino): ")
    return typeOfCoffee

def check_prompt(prompt, money):
    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        return True
    elif prompt == "off":
        return False
    elif prompt == "report":
        for x,y in resources.items():
            print (f"{x}: {y}")
        print(f"Money: {money}")
    else:
        print("Invalid input. Please try again.")



def makeCoffee(prompt, resources):
    money = 0.00
    if resources["coffee"] >= MENU[prompt]['ingredients']['coffee'] and resources["water"] >= MENU[prompt]['ingredients']['water'] and resources["milk"] >= MENU[prompt]['ingredients']['milk']:
        pass
    else:
        print("Sorry there is not enough ingredients to make this coffee")
        return False, resources, money
    print("Please insert coins (quarter = 0.25$, dimes = $0.10, nickles = $0.05, pennies = $0.01 ): ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total >= MENU[prompt]["cost"]:
        change = total - MENU[prompt]["cost"]
        money = total - change
        print(f"Here is ${change:.3f} in change")
        resources["coffee"] -= MENU[prompt]['ingredients']['coffee']
        resources["water"] -= MENU[prompt]['ingredients']['water']
        resources["milk"] -= MENU[prompt]['ingredients']['milk']
        print("Here is your coffee ☕☕☕. Enjoy!")
        return True, resources, money
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, resources, money


Money = 0.00
resources2 = resources
while True:
    prompt = Show_prompt()
    checker = check_prompt(prompt, Money)
    if checker == True:
        check, resources2, money = makeCoffee(prompt, resources2)
        Money += money
    elif checker == False:
        print("Coffee machine is being turned off! GoodBye!")
        break
    else:
        continue