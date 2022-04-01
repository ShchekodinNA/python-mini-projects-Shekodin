import os

MENU = {
    "espresso": {
        "ingredients": {
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.5,
    "pennies": 0.1,
}


def check_res(lv_key):
    """Enter key from MENU and return string with name of not sufficient resource. If all OK - return None"""
    for lv_res in MENU[lv_key]["ingredients"]:
        if resources[lv_res] - MENU[lv_key]["ingredients"][lv_res] < 0:
            return lv_res
    return


while True:
    os.system("cls")
    print("\nWe have:")
    for key in MENU:
        print(f"'{key}' on price: ${MENU[key]['cost']}")

    is_buy = False
    user_input = input("What would you like? (print name): ")
    for key in MENU:
        if user_input == key:
            is_buy = True
            break
    if is_buy:
        rsrc = check_res(user_input)
        if rsrc is not None:
            print(f"Sorry there is not enough {rsrc}")
            continue
        val_sum = 0
        for coin in coins:
            val_sum += int(input(f"how many {coin}?: ")) * coins[coin]
        if val_sum < MENU[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        else:
            resources["money"] += MENU[user_input]["cost"]
            val_sum -= MENU[user_input]["cost"]
            if val_sum != 0:
                print(f"Here is ${val_sum} dollars in change.")
            print(f"Enjoy your {user_input}")
            for res in MENU[user_input]["ingredients"]:
                resources[res] -= MENU[user_input]["ingredients"][res]
    else:
        if user_input == "report":
            print(f"Water:  {resources['water']}ml")
            print(f"Milk:   {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        else:
            print("Have a nice day! Goodbye")
            break
