import random
from hangmanart import stages, logo
from words_list import word_list

hp = len(stages) - 1
word = random.choice(word_list)
word = [char for char in word]

endgame = False

print(logo)

display = ["_" for _ in range(len(word))]

while not endgame:
  print(''.join(display))
  user_input = input("Choose a letter: ").lower()
  if user_input in display:
    print(f"You have already tried the letter {user_input}!")
  elif user_input in word: 
    for i in range(len(word)):
      if user_input == word[i]:
        display[i] = user_input
  else:
    hp -= 1
    if hp == 0:
      print("\nHe died :(")
      endgame = True
  if "_" not in display:
    print("You won!")
    endgame = True
  print(stages[hp])




