import random
from forca_art import logo, stages
from forca_palavras import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
#print(f'Pssst, the solution is {chosen_word}.')

display = []
lives = 6
end_of_game = False
wrong_guesses = []

for i in range(word_length):
    display.append("_")

while not end_of_game:

    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already used the letter " + guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        if guess not in wrong_guesses:
            lives -= 1
            print("The letter " + guess + " is not in the word. You lost a life.")
            print(stages[lives])
            print("lives: " + str(lives))
            wrong_guesses += guess
        else:
            print("You already guessed the letter " + guess + " . It is wrong.")
      
    if "_" not in display:
        print("You win!")
        end_of_game = True

    if (lives == 0):
        print("You lost!")
        print("The word was " + chosen_word)
        end_of_game = True
