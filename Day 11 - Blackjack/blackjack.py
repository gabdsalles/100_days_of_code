import random
from art import logo
import os
 
def clear():
    os.system('cls')

def deal_card():
    """Retorna uma carta aleatória do deck de cartas."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calcula a pontuação a partir de uma lista de cartas do jogador e do computador."""
    score = sum(cards)
    if cards == [11, 10]: #Blackjack
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user_score, computer_score):
    """Compara a pontuação do jogador e do computador para saber quem ganhou a rodada."""
    if user_score == computer_score:
        return "Empate"
    elif user_score == 0:
        return "Você venceu com Blackjack!"
    elif computer_score == 0:
        return "Perdeu, o oponente tem Blackjack"
    elif user_score > 21:
        return "Passou de 21, perdeu!"
    elif computer_score > 21:
        return "O oponente passou de 21, você ganhou!"
    elif user_score > computer_score:
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def play_game():

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"         Suas cartas: {user_cards}, pontuação atual: {user_score}")
        print(f"         Primeira carta do computador: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Digite 's' para pegar outra carta ou 'n' para passar a vez ")
            if user_should_deal == "s":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                while computer_score != 0 and computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                game_over = True

    print(f"         Suas cartas finais: {user_cards}, pontuação final: {user_score}")
    print(f"         Cartas finais do computador: {computer_cards}, pontuação: {computer_score}")

    print(compare(user_score, computer_score))


while input("Quer jogar Blackjack? Digite 's' para sim ou 'n' para não. ") == "s":
    clear()
    print(logo)
    play_game()
