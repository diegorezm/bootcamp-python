#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as file:
    names = [line.rstrip() for line in file]
with open("./Input/Letters/starting_letter.txt") as file:
    template: list[str] = []
    for line in file:
        if line == '':
            pass
        template.append(line)

for name in names:
    new_letter = template
    # for some reason the replace method is not working here, 
    # so im just replacing the entire thing for now
    new_letter[0] = f"Dear {name}\n"
    with open(f"./Output/ReadyToSend/letter_{name}.txt", "w") as file:
        for line in new_letter:
            file.write(line)
