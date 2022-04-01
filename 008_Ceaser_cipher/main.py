import string
from art import logo

def ceaser_cipher(text, shift, direct, alphabet):
    text_list = list(text)
    some = shift // len(alphabet)
    if int(some) != 0:
        shift = shift - int(some)*len(alphabet)
    if direct == "d": shift *= -1
    for i in range(len(text_list)):
        index_al = alphabet.index(text_list[i])
        if index_al + shift >= len(alphabet):
            index = index_al + shift - len(alphabet)
        elif index_al + shift < 0:
            index = index_al - shift 
        else : index = index_al + shift
        text_list[i] = alphabet[index]
    return "".join(text_list)
alphabet = list(string.ascii_lowercase)
# begin \/
print(logo)
direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
if direction != "e" and direction != "d":
    print("You chosen wrong direction!")
    quit()
    
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "e":
    print(f"Encrypted message: {ceaser_cipher(text,shift,'e',alphabet)}")
else:
    print(f"Decoded message:   {ceaser_cipher(text,shift,'d',alphabet)}")