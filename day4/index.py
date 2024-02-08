import random
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

entries = ["rock", "paper", "scissors"]

def get_random_entry():
    idx = random.randint(0, len(entries) - 1)
    return entries[idx]

def get_entry_rep(entry: str):
    match entry:
        case "rock":
            return rock
        case "paper":
            return paper
        case "scissors":
            return scissors
        case _:
            return scissors

def get_winner(computer: str, user: str):
    if computer == user:
        return "Game ended in a draw!"
    match user:
        case "rock":
            if computer == entries[1]:
                return "Paper covers rock! you loose!"
            else:
                return "Rock smashes scissors! you win!"
        case "paper":
            if computer == entries[0] :
                return "Paper covers rock! you win!"
            else:
                return "scissors cut paper! you loose!"
        case "scissors":
            if computer == entries[0] :
                return "Rock smashes scissors! you loose!"
            else:
                return "scissors cut paper! you win!"

def loading_screen(message: str):
    print(message, end='', flush=True)
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

user_input = input("Rock, paper or scissors? ")
if user_input not in entries:
    print("Not a valid input!")
    exit(1)

computer_input = get_random_entry()

print(f"You choose {user_input}....\n {get_entry_rep(user_input)}")
print(f"\nThe computer choose {computer_input}\n {get_entry_rep(computer_input)}")
loading_screen(message="And the results are")
print(get_winner(computer_input, user_input))
