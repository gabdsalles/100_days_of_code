from art import logo, vs
from game_data import data
import os
import random
 
def clear():
    os.system('cls')

def pick_random_name():
    return random.choice(data)

def check_escolha(a, b, escolha):

    if (escolha == "A" and a > b) or (escolha == "B" and b > a):
        return True
    else: #elif (escolha == "A" and b > a) or (escolha == "B" and a > b)
        return False

def game():

    points = 0

    while (True):

        print(logo)

        if points != 0:
            print(f"Você acertou! Pontuação atual: {points}")
            escolha_A = escolha_B
        else:
            escolha_A = pick_random_name()

        escolha_B = pick_random_name()

        while (escolha_B == escolha_A):
            escolha_B = pick_random_name()

        print(f"Compare A: {escolha_A['name']}, um (a) {escolha_A['description']}, do país {escolha_A['country']}\n{vs}")
        print(f"Com B: {escolha_B['name']}, um (a) {escolha_B['description']}, do país {escolha_B['country']}")
        escolha_jogador = input("Quem tem mais seguidores? Digite 'A' ou 'B' ").upper()
        resultado = check_escolha(escolha_A['follower_count'], escolha_B['follower_count'], escolha_jogador)

        if (resultado):
            points += 1
        else:
            clear()
            print(logo)
            print(f"Fim de jogo.\nVocê finalizou o jogo com {points} pontos.")
            return
        
        clear()
    
game()