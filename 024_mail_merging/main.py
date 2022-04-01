# TODO: Create a letter using starting_letter.txt
#   for each name in invited_names.txt

with open("Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()
files_list = []

for name in name_list:
    name = name.strip()
    with open(f"Output/ReadyToSend/{name}_congrats.txt", mode="w") as file:
        file.write(letter_template.replace("[name]", name))




#   Replace the [name] placeholder with the actual name.








#   Save the letters in the folder "ReadyToSend".



# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



