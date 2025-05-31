import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pandas

#--------------------------------- form management ------------------------------------------#
def get_login():
    df = pandas.read_csv("skeaneRW/day29/passwd.csv")
    if not df.empty:
        return df.login.max()
    else:
        return ""

def reset_form():
    site_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    validation_label.config(text="")

def validate_form():
    # check that all fields are filled.
    has_site = len(site_entry.get()) > 0
    has_login = len(login_entry.get()) > 0
    has_pass = len(pass_entry.get()) > 0
    if not all ([has_site, has_login, has_pass]):
        validation_label.config(text="complete all entries before adding a new password.")
        return False
    else:
        return True


#--------------------------------- command buttons ----------------------------------------#
def click_add():
    if validate_form():
        df = pandas.read_csv("skeaneRW/day29/passwd.csv")
        site = site_entry.get()
        login = login_entry.get()
        passwd = pass_entry.get()
        df.loc[len(df)] = {"site":site, "login":login, "passwd":passwd}
        proceed_to_add = messagebox.askokcancel(title="password for {site}", message=f"add the following password:\nsite: {site}\nlogin: {login}\n password: {passwd}")
        if proceed_to_add:
            df.to_csv("skeaneRW/day29/passwd.csv", index=False)
            reset_form()
        else:
            return

def generate_pass():
    pass_entry.delete(0, tk.END)

    num_list = [str(randint(0,9)) for _ in range(randint(2,4))]
    ucase_list = [choice(string.ascii_uppercase) for _ in range(randint(2,5))]
    lcase_list = [choice(string.ascii_lowercase) for _ in range(randint(2,5))]
    special_list = [choice(string.punctuation) for _ in range(randint(2,4))]
    
    new_pass_list = num_list + ucase_list + lcase_list + special_list
    
    shuffle(new_pass_list)
    
    pass_entry.insert(0, ''.join(new_pass_list))

#---------------------------------- app layout --------------------------------------------#
window = tk.Tk()
window.title("Python Password Manager")

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="skeaneRW/day29/logo.png")
canvas.create_image(100,95, image=lock_img)
canvas.grid(row=0, column=1)

site_label = tk.Label(text="website")
site_label.grid(row=1, column=0, sticky="E", padx=10)
site_entry = tk.Entry()
site_entry.grid(row=1, column=1, columnspan=2, sticky="WE", padx=15)
site_entry.focus()

login_label = tk.Label(text="email/username")
login_label.grid(row=2, column=0, sticky="E", padx=10)
login_entry = tk.Entry()
login_entry.grid(row=2, column=1, columnspan=2, sticky="WE", padx=15)
login_entry.insert(0,get_login())

pass_label = tk.Label(text="website")
pass_label.grid(row=3, column=0, sticky="E", padx=10)
pass_entry = tk.Entry()
pass_entry.grid(row=3, column=1, sticky="WE", padx=15)
pass_button = tk.Button(text="Generate Password", command=generate_pass)
pass_button.grid(row=3, column=2, sticky="WE", padx=15)

add_button = tk.Button(text="Add", command=click_add)
add_button.grid(row=4, column=0, columnspan=3, sticky="WE", padx=20, pady=5)

validation_label = tk.Label(text="", foreground="#C30E59")
validation_label.grid(row=5, column=0, columnspan=3, sticky="WE", padx=10, pady=5)

window.mainloop()