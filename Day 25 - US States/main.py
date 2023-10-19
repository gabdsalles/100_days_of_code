import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = './Day 25 - US States/blank_states_img.gif'

df = pd.read_csv('./Day 25 - US States/50_states.csv')
list_states = df['state'].to_list()
#print(list_states)

screen.addshape(image)
turtle.shape(image)

score = 0

estados_corretos = []

def desenhar_nome_estado(resposta):

    index = list_states.index(resposta)
    state_data = df[df.state == resposta]
    x = int(state_data.x)
    y = int(state_data.y)
    new_turtle = turtle.Turtle()
    new_turtle.pu()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(resposta)

def generate_csv():
    
    #aplicando list comprehension
    estados_nao_aprendidos = [state for state in list_states if state not in estados_corretos]

    df_states = pd.DataFrame(estados_nao_aprendidos)
    df_states.to_csv('./Day 25 - US States/states_to_learn.csv')


while score < 50:

    resposta = screen.textinput(title=f"{score}/50 estados", prompt="Qual é outro nome de um estado?").title()
    if resposta in list_states and resposta not in estados_corretos:
        desenhar_nome_estado(resposta)
        estados_corretos.append(resposta)
        score += 1
    if resposta == 'Exit':
        generate_csv()
        break