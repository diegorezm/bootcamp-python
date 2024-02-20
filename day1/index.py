import random

name = input("Your name:\n")
pet = input("The name of your pet:\n")

data = [name, pet]


def get_random_index():
    return random.randint(0, 1)


print(f"Your band name can be {data[get_random_index()]} {data[get_random_index()]}")
