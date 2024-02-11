import os
from random import choice
from typing import List
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(hand: List[int]):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
       hand.remove(11) 
       hand.append(1)
    return sum(hand)

user_hand = []
computer_hand = []

for _ in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())



def game():
    endgame = False
    user_final_score = calculate_score(user_hand)
    computer_final_score = calculate_score(computer_hand)
    print(logo)
    while not endgame:
        print(f"Your cards: {user_hand}")
        print(f"Computer first card: {computer_hand[0]}")
        user_final_score = calculate_score(user_hand)
        computer_final_score = calculate_score(computer_hand)
        if user_final_score == 0 or computer_final_score == 0 or user_final_score > 21:
            endgame = True
        more_cards = input('Do you want to draw more cards? (Y\\n) ').lower()
        if more_cards == "n":
            endgame = True
        else:
            user_hand.append(deal_card())
    print(f"Your final hand: {user_hand}\nComputer final hand: {computer_hand}")

    if user_final_score > computer_final_score:
        print("You win! :)")
    elif user_final_score == computer_final_score:
        print("Draw! >:o")
    else:
        print("You loose! :(")

if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? (Y\\n) ").lower() == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        game()

