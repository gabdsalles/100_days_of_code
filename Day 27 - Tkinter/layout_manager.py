from tkinter import *

#Criar janela
window = Tk()
window.title('My first GUI using Tkinter')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #padding

#Criar label (rótulos)

my_label = Label(text="I am a label", font=('Arial', 24, 'italic'))
#my_label.pack() #essa linha faz que a label seja mostrada na tela
my_label.grid(column=0, row=0)

def button_clicked():
    print("I got clicked")
    my_label['text'] = input.get()
    

#botão
my_button = Button(text="Click me")
my_button.config(command=button_clicked)
my_button.grid(column=1, row=1)

new_button = Button(text="I'm another button")
new_button.config(command=button_clicked)
new_button.grid(column=2, row=0)

#entrada de dados
input = Entry()
input.grid(column=3, row=2)


window.mainloop()