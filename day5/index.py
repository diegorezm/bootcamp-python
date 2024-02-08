import string
import random
from typing import List

print("Welcome to the PyPassword Generator!\n")


nr_letters = int(input("How many letters do you want in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password_list: List[str] = []

alphabet = list(string.ascii_lowercase + string.ascii_uppercase)  
symbols = ["%", "@", "#", "$", "&", "*","(", ")", "-", "_", "+", "-"]
possible_numbers = list(range(101))

def get_random_letter():
    return random.choice(alphabet)

def get_random_number():
    return random.choice(possible_numbers)

def get_random_symbol():
    return random.choice(symbols)

for _ in range(nr_letters - 1):
    password_list.append(get_random_letter())

for _ in range(nr_symbols - 1):
    password_list.append(get_random_symbol())

for _ in range(nr_numbers - 1):
    password_list.append(str(get_random_number()))

random.shuffle(password_list)
password = ''.join(password_list)
print(f"Here is you password: {password}")
