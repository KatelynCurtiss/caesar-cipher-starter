# Katelyn Curtiss
# October 4 2024
# Caesar Cipher Starter

alphabet = "abcdefghijklmnopqrstuvwxyz"

user_message = input("Enter your secret message: ")
print(user_message)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_postion = (position + key) % 26 
        new_character = alphabet[new_postion]