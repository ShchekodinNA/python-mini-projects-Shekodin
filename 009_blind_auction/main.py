from art import logo
import os
Dict = {}
def auto_add():
    lv_name = input("What is your name?: ")
    lv_bid = int(input("What's your bid?: $"))
    Dict[lv_name] = lv_bid 
    
print(logo)
print("Welcome to the secret auction program.")
auto_add()
while input("Are there any other bidders? Type 'y' or 'n'\n") == 'y':
    os.system("cls")
    auto_add()
os.system("cls")
max_bid = 0
for name in Dict:
    if Dict[name] > max_bid:
        max_bid = Dict[name]
        name = name

print(f"The winner is {name} with a bid of ${max_bid}")