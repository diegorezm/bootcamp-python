line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input() 
position = position.upper()
letters = ["A", "B", "C"]
letter_idx = letters.index(position[0])
letter_position = int(position[1]) - 1

map[letter_position][letter_idx] = "X"
print(f"{line1}\n{line2}\n{line3}")
