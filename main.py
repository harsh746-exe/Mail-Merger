#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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




