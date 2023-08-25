import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
is_game_over = False

def choose_number():
    return random.randint(1, 100)

def compare(guess, number):

    if guess > number:
        return "Muito alto!\nAdivinhe novamente"
    elif guess < number:
        return "Muito baixo!\nAdivinhe novamente."
    else:
        return "ganhou"
    
def set_dificuldade():
    dificuldade = input("Escolha uma dificuldade. Digite 'facil' ou 'dificil', sem acentos.")
    if dificuldade == "facil":
        return EASY_ATTEMPTS
    elif dificuldade == "dificil":
        return HARD_ATTEMPTS

print(logo)
print("Seja bem-vindo ao Adivinhe o Número!\nEstou pensando em um número entre 1 e 100")
number = choose_number()
attempts = set_dificuldade()
# print(f"Pssst, a resposta correta é {number}")

while attempts > 0 and not is_game_over:
    guess = int(input("Adivinhe um número: "))

    message = compare(guess, number)

    if message == "ganhou":
        is_game_over = True
        print(f"Você conseguiu! A resposta é {number}")
    else:
        print(message)
        attempts -= 1
        print(f"Você tem {attempts} tentativas restantes para adivinhar o número.")

if (attempts == 0):
    print("Suas tentativas acabaram! Você perdeu")

    
