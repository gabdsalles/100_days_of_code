from tkinter import *

#Criar janela
window = Tk()
window.title('My first GUI using Tkinter')
window.minsize(width=500, height=300)

#Criar label (rótulos)

my_label = Label(text="I am a label", font=('Arial', 24, 'italic'))
my_label.pack() #essa linha faz que a label seja mostrada na tela

def button_clicked():
    print("I got clicked")
    my_label['text'] = input.get()
    

#botão
my_button = Button(text="Click me")
my_button.config(command=button_clicked)
my_button.pack()

#entrada de dados
input = Entry()
input.pack()


window.mainloop()