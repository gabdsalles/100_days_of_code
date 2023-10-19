names_file = open("./Day 24 - Mail Merge/Input/Names/invited_names.txt")
names = names_file.readlines()
#print(names)

for name in names:
    letter_text = open("./Day 24 - Mail Merge/Input/Letters/starting_letter.txt")
    new_letter = open("./Day 24 - Mail Merge/Output/ReadyToSend/letter_for_" + name.strip() + ".txt", mode="w")
    letter_content = letter_text.read()
    letter_content = letter_content.replace("[name]", name.strip())
    new_letter.write(letter_content)


names_file.close()