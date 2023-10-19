from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    if (direction == "decode"):
        shift *= -1
    for letter in text:
        if (letter in alphabet): #é uma letra do alfabeto, tem que trocar
            index = alphabet.index(letter) + shift
            if (index >= len(alphabet)): #se for uma letra no final da lista
                index = index - len(alphabet)
            new_text += alphabet[index]
        else: #só copiar
            new_text += letter
    print(f"The {direction}d text is " + new_text)

print(logo)

direction = "yes"

while (direction == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift % 26, direction)
    direction = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

print("Goodbye")