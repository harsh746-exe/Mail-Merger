
with open("./Input/Names/invited_names.txt", mode="r") as names:
    lists = names.readlines()
    lines = []
    for element in lists:
        lines.append(element.strip())
    print(lines)
    for name in lines:
        with open("./Input/letters/starting_letter.txt") as f:
            letter = f.read()
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w+") as new_letter:
                # print(l)
                new_letter.write(letter.replace("[name]", name))
                # new_letter.write(letter)
                upd = new_letter.read()




