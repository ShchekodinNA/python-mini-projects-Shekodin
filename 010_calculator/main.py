from art import logo
import os

def substract(lftn, rign):
    return lftn - rign

def add(lftn, rign):
    return lftn + rign

def multiply(lftn, rign):
    return lftn * rign

def divide(lftn, rign):
    if rign == 0: return
    return lftn / rign


operations = {
    "+" : substract,
    "-" : add,
    "*" : multiply,
    "/" : divide,
}

def calculation():
    
    os.system("cls")
    print(logo)
    l_nmb = float(input("What's the first number?: "))
    cntn = True
    while cntn:
        operator = input("('+', '-', '*', '/')Pick an operation: ")
        r_numb = float(input("What's the second number?: "))
        answ = operations[operator](l_nmb,r_numb)
        print(f"{l_nmb} {operator} {r_numb} = {answ}")
        choise =input(f"Type 'y' to continue with {answ}, "+
                "or 'n' to start a new calculation. Other symbol - exit: ") 
        if choise == 'n':
            calculation()
        elif choise == 'y':
            l_nmb = answ
        else : cntn = False


calculation()   