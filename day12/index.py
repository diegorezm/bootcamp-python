from random import randint
import os


def game():
    number = randint(1,101)
    print("Welcome to  the number guessing game!\nIm thiking of a number between 1 and 100....")
    difficulty = input("Choose a difficulty: (easy\\hard) ")
    attempts = 10 if difficulty == "easy" else 5
    while attempts > 0: 
        user_number = int(input("Make a guess: "))
        print(f"You have {attempts} remaining attempts.")
        if user_number == number:
            print("You won!!")
            break
        else:
            attempts -= 1
            if user_number > number:
                print("Too high.")
            elif user_number < number:
                print("Too low.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    game()

