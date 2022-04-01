import random
from art import logo
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10]

def add_card(curr_cards):
    curr_card = random.choice(cards)
    if curr_card == 11 and curr_card + sum(curr_cards) > 21:
        curr_card = 1
    return [curr_card]

choose = input("Do you want to play blackjack ('y','n')?: ")

os.system("cls")
print(logo)
y_cards = []
d_cards = []
d_cards += add_card(d_cards) + add_card(d_cards)
y_cards += add_card(y_cards) + add_card(y_cards)
print(f"Your cards: {y_cards}, score: {sum(y_cards)}")
print(f"Dealer card: {d_cards[0]}, score: {d_cards[0]}")
whowin = 0
while True:
    subchoose = input("Type 'y' to get another card, type 'n' to pass: ")
    if subchoose == "y":
        y_cards += add_card(y_cards)
        print(f"Your Cards: {y_cards}, score {sum(y_cards)}")
    else: 
        break
    if sum(y_cards) > 21:
        whowin = -1
        break
while sum(d_cards) < 17 and whowin >= 0:
    d_cards += add_card(y_cards)
    if sum(y_cards) > 21:
        whowin = 1
        break
print(f"Dealer final hand: {d_cards}, score {sum(d_cards)}")
if whowin == 0:
    if sum(y_cards) > sum(d_cards):
        whowin = 1
    elif sum(y_cards) < sum(d_cards):
        whowin = - 1
if whowin == 0:
    print("Draw!")
elif whowin == 1:
    print("You Win!")
else:
    print("Dealer Win!")
