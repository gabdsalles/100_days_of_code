import pandas as pd

#TODO 1. Create a dictionary in this format:
df_nato = pd.read_csv('./Day 26 - NATO/nato_phonetic_alphabet.csv')

dict_nato = {row.letter:row.code for (index, row) in df_nato.iterrows()}
print(dict_nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
program_is_on = True

while program_is_on:
    word = input("Insira uma palavra: ").upper()
    try:
        result = [dict_nato[letter] for letter in word] #dicionário na chave que possui tal letra
    except KeyError:
        print("Desculpe, apenas letras neste alfabeto.")
    else:
        program_is_on = False


print(result)

