import random
import os
words = ["mouse", "hangman", "german", "table", "sophisticated"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = []
for i in random.choice(words):
    word.append([i,False])
health = 6
letter = ""
step = True
while  health >= 1:
    os.system("cls")
    win = True
    for i in word:
        if i[0] == letter or i[1] :
            print(i[0], end = " ")
            if i[0] == letter:
                step = i[1] = True       
        else:
            print("_", end = " ")
            win = False
    print("")        
    if not step:
        health -=1
        print(f"Its wrong letter! You have {health} attempts.")
    
    
    print(stages[health])
        
    if win:
        print("You win!")
        quit()
        
    letter = input("insert a letter: ")[0].lower()
    step = False
    print(stages[health])

print("You lose!")    
