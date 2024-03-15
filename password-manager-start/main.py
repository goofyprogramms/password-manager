from tkinter import *
from random import choice, randint, shuffle
import pyperclip
from tkinter import messagebox
import pandas as pd

df = pd.DataFrame()
text_file = 'data.txt'
df.to_csv(text_file, sep='\t', index=False)

print("Empty text file created successfully:", text_file)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_button_function():
    web_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if len(web_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Ooops", message="do not leave any entries empty")

    else:

        is_ok = messagebox.askokcancel(
            title=web_text, message=f"these are the details\n Email: "
                                    f"{email_text}\n password: {password_text}\n do you want to continue?")

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{web_text} | {email_text} | {password_text} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "salehsal788@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=add_button_function)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
