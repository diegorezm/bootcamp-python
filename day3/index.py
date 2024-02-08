print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island. Your mission is to find the treasure!")
path = input("You have two paths, left or right, witch one do you choose? ")

match path:
    case "left":
        path = input("You have encountered a river, would you like to swim or wait? ")
        match path:
            case "swim":
                print("Attacked by trout.Game Over.")
            case "wait":
                path = input("You have encountered tree doors, one is red the other one is blue and the last one is yellow. Wich one do you choose? ")
                if path == "blue":
                    print("Eaten by beasts.Game Over.")
                    exit(1)
                elif path == "red":
                    print("Burned by fire.Game Over.")
                    exit(1)
                elif path == "yellow":
                    print("You win!")
                    exit(0)
                else:
                    print("Wrong! you are dead now!")
                    exit(1)

            case _:
                print("Wrong! you are dead now!")
                exit(1)

    case "right":
        print("Fall into a hole.Game Over.")
        exit(1)
    case _:
        print("Wrong! you are dead now!")
        exit(1)
