from typing import List
from art import logo
from Person import Person
print(logo)
print("Welcome to the secret auction program.")
endgame = False

winner_bid = 0
winner_name = ""

# I don't need this
bidders: List[Person] = []

while not endgame:
    new_name = input("What is your name? ")
    new_bid  = int(input("What is your bid? $"))
    new_person = Person(name=new_name, bid=new_bid)
    if new_bid > winner_bid:
        winner_bid = new_bid
        winner_name = new_name
    # Useless code, did this as a test
    bidders.append(new_person)
    new_bidders = input("Are there any new bidders? Type 'yes' or 'no'\n").lower()
    while new_bidders not in ["yes", "no"]:
        new_bidders = input("Please type 'yes' or 'no'\n").lower()
    if new_bidders == "no":
        endgame = True

import time
def loading_screen(message: str):
    print(message, end='', flush=True)
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.5)
loading_screen("And the winner is")
print(f"\n{winner_name} with ${winner_bid}!")
print(bidders)

