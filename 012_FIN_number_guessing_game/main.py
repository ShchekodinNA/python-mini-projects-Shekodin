from asyncio import Handle
import my_art
import random
import os
EASY_H = 10
HARD_H = 5
def gme():
    """Little game (Guess the number)"""
    os.system("cls")
    number = random.randint(1,100)
    print(my_art.numb_guess_logo)
    print("I'm thinking of a number between 1 and 100.")
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy" :
        health = EASY_H
    else: 
        health = HARD_H

    while health > 0 :
        print(f"You have {health} attempts remaining to guess the number.")
        in_number = int(input("Make a guess: "))
        if in_number == number:
            print(my_art.win)
            quit()
        elif in_number < number:
            print("Too low!\nGuess again.")
        else:
            print("Too heigh!\nGuess again.")
        health -= 1
    return
gme()