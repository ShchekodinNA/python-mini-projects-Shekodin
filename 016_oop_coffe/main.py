from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
lo_menu = Menu()
lo_money_machine = MoneyMachine()
lo_cff_mkr = CoffeeMaker()
print()

while True:
    print("/nWe have:")
    for obj in lo_menu.menu:
        print(f"{obj.name} on price: ${obj.cost}")
    user_input = input("What would you like? (print name): ")
    if user_input in lo_menu.get_items():
        lo_mn_itm = lo_menu.find_drink(user_input)
        if not lo_cff_mkr.is_resource_sufficient(lo_mn_itm):
            continue
        if lo_money_machine.make_payment(lo_mn_itm.cost):
            lo_cff_mkr.make_coffee(lo_mn_itm)
        else:
            continue
    else:
        if user_input == "report":
            lo_cff_mkr.report()
            lo_money_machine.report()
        else:
            print("Have a nice day! Goodbye")
            break
