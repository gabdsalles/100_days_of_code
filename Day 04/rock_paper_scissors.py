import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
random.seed()
imagens_jogo = [pedra, papel, tesoura]
players_choice = int(input("Seja bem-vindo ao jogo Pedra, Papel e Tesoura!\nQual você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))

if (players_choice > 2):
    print("Escolha inválida")
    exit()
else:
    print("\n" + imagens_jogo[players_choice])

print("\n\nComputador escolheu: \n")

computers_choice = random.randint(0, 2)

# print(computers_choice)

print("\n" + imagens_jogo[computers_choice] + "\n")

if (players_choice == computers_choice):
    print("É um empate!")
else:
    combination = int(str(players_choice) + str(computers_choice))
    print(combination)
    computers_win_combination = [1, 12,20]
    players_win_combination = [2, 10, 21]
    if (combination in players_win_combination):
        print("Você ganhou! Parabéns :)")
    elif (combination in computers_win_combination):
        print("O computador ganhou! Você perdeu :(")

