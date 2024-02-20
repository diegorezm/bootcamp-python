from art import logo

print(logo)


def plus(n1: int, n2: int):
    """THIS FUNCTION ADDS TWO NUMBERS"""
    return n1 + n2


def minus(n1: int, n2: int):
    """THIS FUNCTION SUBTRACTS TWO NUMBERS"""
    return n1 - n2


def times(n1: int, n2: int):
    """THIS FUNCTION MULTIPLY TWO NUMBERS"""
    return n1 * n2


def devide(n1: int, n2: int):
    """THIS FUNCTION DIVIDES TWO NUMBERS"""
    return n1 / n2


operations = ["+", "-", "*", "/"]

n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))

endgame = False

while not endgame:
    print("\n".join(operations))
    op = input("Pick an operation: ")
    while op not in operations:
        op = input("Pick a valid operation: ")
    match op:
        case "+":
            results = plus(n1, n2)
            print(f"{n1} + {n2} = {results}")
        case "-":
            results = minus(n1, n2)
            print(f"{n1} - {n2} = {results}")
        case "/":
            results = devide(n1, n2)
            print(f"{n1} / {n2} = {results}")
        case "*":
            results = times(n1, n2)
            print(f"{n1} * {n2} = {results}")
        case _:
            print("NOT A VALID OPERATION!")
    user_continue = input(
        f"Type 'y' to keep using {n1} and {n2}, type 'n' to start a new calculation. (type exit to get out): "
    ).lower()
    while user_continue not in ["y", "n", "exit"]:
        user_continue = input("Not a valid input, please provide 'y' or 'n'.")
    if user_continue == "n":
        n1 = int(input("What is the first number? "))
        n2 = int(input("What is the second number? "))
    elif user_continue == "exit":
        endgame = True
