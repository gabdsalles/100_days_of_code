from tkinter import *

window = Tk()
window.title('Conversor de milhas para km')
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

miles_label = Label(text='Milhas')
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="é igual a")
is_equal_label.grid(row=1, column=0)

result_label = Label(text='0')
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def button_clicked():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=str(f"{km}"))

calculate_button = Button(text="Calcular", command=button_clicked)
calculate_button.grid(row=2, column=1)



window.mainloop()