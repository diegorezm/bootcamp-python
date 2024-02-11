import os
from random import choice
from art import logo, vs
from data import data

def get_random_data():
    return choice(data)

def game():
    print(logo)
    a = get_random_data()
    b = get_random_data()
    user_score = 0
    while True:
        print(f"Compare A: {a.name}, a {a.description} from {a.country}")
        print(vs)
        print(f"Against B: {b.name}, a {b.description} from {b.country}")
        user_guess = input("Who has more followers? (A\\B) ").lower()
        while user_guess not in ["a", "b"]:
            user_guess = input("Who has more followers? (A\\B) ").lower()
        if user_guess == "a" and a.follower_count > b.follower_count:
            user_score += 1
            print(f"You won! Your current score is: {user_score}")
        elif user_guess == "b" and b.follower_count > a.follower_count:
            user_score += 1
            print(f"You won! Your current score is: {user_score}")
        else:
            print(f"You lost!\nYour final score was: {user_score}")
            break

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    game()
