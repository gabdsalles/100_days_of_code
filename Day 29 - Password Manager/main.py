from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_characters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_characters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    string = f"{website} - {email} - {password}"
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if (website == "" or password == ""):
       messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("./Day 29 - Password Manager/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./Day 29 - Password Manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("./Day 29 - Password Manager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    
    website = website_entry.get()

    try:
        with open("./Day 29 - Password Manager/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            with open("./Day 29 - Password Manager/data.json", "w") as data_file:
                pass #só cria o arquivo
            messagebox.showinfo(title="Arquivo não encontrado", message="Data file não encontrado.")
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="Site não encontrado", message=f"O site {website} não tem email e senha salvos")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="./Day 29 - Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry = Entry(width=27)
email_username_entry.grid(row=2, column=1)
email_username_entry.insert(END, "gabriel@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_entry.insert(END, generate_password())

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(width=15, text="Search", command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()