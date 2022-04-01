with open("Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()
files_list = []

for name in name_list:
    name = name.strip()
    with open(f"Output/ReadyToSend/{name}_congrats.txt", mode="w") as file:
        file.write(letter_template.replace("[name]", name))

