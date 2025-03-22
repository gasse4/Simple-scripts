import random
import string

def generate_password(length , numbers = True , special_chars = True):
    password = ''
    characters = string.ascii_letters
    number = string.digits
    special = string.punctuation
    
    if numbers:
        characters += number
    if special_chars:
        characters += special
        
    for i in range(length):
        password += random.choice(characters)
    return password


lgth = int(input("Enter the length of the password: "))
nums = input("Do you want numbers in the password? (y/n): ").strip().lower()== 'y'
specials = input("Do you want special characters in the password? (y/n): ").strip().lower() == 'y'


print(generate_password(lgth, nums, specials))