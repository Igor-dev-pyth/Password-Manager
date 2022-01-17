from tkinter import *
from tkinter import messagebox
import random
# How to make the generated password immediately saved in the memory and ready to paste:
import pyperclip

import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # How to make the generated password immediately saved in the memory and ready to paste:
    pyperclip.copy(password)
# ---------------------------- SEARCH DATA ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No such file found")
    else:
        for key,value in data.items():
            if key == website:
                messagebox.showinfo(title=website, message=f"Name: {data[key]['email']}\n "
                                                            f"Password: {data[key]['password']}")
            else:
                messagebox.showinfo(title="Error!", message=f"No details for the {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = name_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Stop!", message=f"Please fill the empty spaces")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else: # The code that needs to be run if there are no issues
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # Saving the updated data (writing something new to the data.json)
                json.dump(data, file, indent=4)
        finally: # No matter if there were an issue or not
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_button = Button(width=15, text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(width=30, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(width=15, text="Search", command=find_password)
search_button.grid(column=2, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
# When launch a program, cursor will be on this entry
website_entry.focus()

name_entry = Entry(width=40)
name_entry.grid(column=1, row=2, columnspan=2)
# When launch a program, some email will already be filled
name_entry.insert(0, "igor@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()