# imports
import tkinter as ttk
from tkinter import messagebox

# Window and layout of buttons and screen
screen = ttk.Tk()
screen.title("Password Manager")
screen.minsize(width=450, height=100)
screen.config(padx=50, pady=50)
website_label = ttk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = ttk.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_label = ttk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = ttk.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "")
password_label = ttk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = ttk.Entry(width=21)
password_input.grid(column=1, row=3)


# Button to get password and password save
def pass_save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    filename = website + email
    with open(filename, "w") as file:
        file.write(f"{website}\n")
        file.write(f"{email}\n")
        file.write(f"{password}")
        website_input.delete(0, "end")
        password_input.delete(0, "end")
        website_input.focus()
        file.close()


def get_pass():
    website = website_input.get()
    email = email_input.get()
    filename = website + email
    with open(filename, "r") as file:
        tempvar = file.readlines()
        messagebox.showinfo(title="PRE SAVED INFORMATION",
                            message=f"Website: {tempvar[0]}\nEmail: {tempvar[1]}\nPassword: {tempvar[2]}")
        file.close()


# work of buttons
button = ttk.Button(text="Save Password", command=pass_save)
button.grid(column=0, row=5, columnspan=2)
button2 = ttk.Button(text="Get Password", command=get_pass)
button2.grid(column=2, row=5, columnspan=2)

# trust me I don't know why this is here
screen.mainloop()
