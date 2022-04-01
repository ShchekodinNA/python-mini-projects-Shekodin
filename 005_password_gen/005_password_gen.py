#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_length = int(input("Input password length (>2): "))
nr_letters = random.randint(1,nr_length-2)
nr_symbols = random.randint(1,nr_length-nr_letters-1)
nr_numbers = nr_length-nr_letters-nr_symbols

password = []
for i in range(0,nr_letters):
    password += [random.choice(letters)]

for i in range(0,nr_symbols):
    password += [random.choice(numbers)]
for i in range(0,nr_numbers):
    password += [random.choice(symbols)]  
random.shuffle(password)
password = "".join(password)
print(password)

