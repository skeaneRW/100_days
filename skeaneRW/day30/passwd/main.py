import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import json

FILE_PATH = "skeaneRW/day30/passwd/data.json"

#--------------------------------- form management ------------------------------------------#
def get_login():
    try:    
        with open(FILE_PATH, "r") as file:
            pass_dict = json.load(file)
            login_list = [ pass_dict[key]["login"] for key in pass_dict ]
            return(max(login_list))
    except (FileNotFoundError, json.JSONDecodeError):
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
        site = site_entry.get()
        login = login_entry.get()
        passwd = pass_entry.get()
        new_entry = {
        site: {
            "login": login,
            "passwd": passwd,
            },
        }
        try:
            with open(FILE_PATH, "r") as file:
                data = json.load(file)
                data.update(new_entry)
        except(FileNotFoundError, json.JSONDecodeError):
            with open(FILE_PATH, "w") as new_file:
                json.dump(new_entry, new_file, indent=4)
        else:
            with open(FILE_PATH, "w") as file:
                json.dump(data, file, indent=4)
        finally:
            reset_form()

def generate_pass():
    pass_entry.delete(0, tk.END)

    num_list = [str(randint(0,9)) for _ in range(randint(2,4))]
    ucase_list = [choice(string.ascii_uppercase) for _ in range(randint(2,5))]
    lcase_list = [choice(string.ascii_lowercase) for _ in range(randint(2,5))]
    special_list = [choice(string.punctuation) for _ in range(randint(2,4))]
    
    new_pass_list = num_list + ucase_list + lcase_list + special_list
    
    shuffle(new_pass_list)
    
    pass_entry.insert(0, ''.join(new_pass_list))

def site_search():
    seach_term = site_entry.get()
    notFoundMessage = messagebox.showinfo(title=f"{seach_term} login details", message=f"no password found for {seach_term}")
    if seach_term == "":
        messagebox.showinfo(title="missing site", message="please enter website name")
        return
    try:
        with open(FILE_PATH, "r") as file:
            login_data = json.load(file)
            sites_list = [key for key, _ in login_data.items() if seach_term.lower() in key.lower()]
            results_message = [f"site: {site}\nlogin: {login_data[site]["login"]}\npassword: {login_data[site]["passwd"]}\n" for site in sites_list]
            results_message = '\n'.join(results_message)
            if len(sites_list):
                messagebox.showinfo(title=f"{seach_term} login details", message=results_message)
            else:
                notFoundMessage
    except(KeyError, json.JSONDecodeError):
        notFoundMessage
    pass

#---------------------------------- app layout --------------------------------------------#
window = tk.Tk()
window.title("Python Password Manager")

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="skeaneRW/day30/passwd/logo.png")
canvas.create_image(100,95, image=lock_img, anchor="center")
canvas.grid(row=0, column=0, columnspan=3)

site_label = tk.Label(text="website")
site_label.grid(row=1, column=0, sticky="E", padx=10)
site_entry = tk.Entry(width=25)
site_entry.grid(row=1, column=1, sticky="WE", padx=5)
site_entry.focus()
site_search = tk.Button(text="Search", command=site_search)
site_search.grid(row=1, column=2, sticky="WE", padx=15)

login_label = tk.Label(text="email/username")
login_label.grid(row=2, column=0, sticky="E", padx=10)
login_entry = tk.Entry(width=25)
login_entry.grid(row=2, column=1, columnspan=2, sticky="W", padx=5)
login_entry.insert(0,get_login())

pass_label = tk.Label(text="website")
pass_label.grid(row=3, column=0, sticky="E", padx=10)
pass_entry = tk.Entry(width=25)
pass_entry.grid(row=3, column=1, sticky="WE", padx=5)
pass_button = tk.Button(text="Generate Password", command=generate_pass)
pass_button.grid(row=3, column=2, sticky="WE", padx=15)

add_button = tk.Button(text="Add", command=click_add)
add_button.grid(row=4, column=0, columnspan=3, sticky="WE", padx=20, pady=5)

validation_label = tk.Label(text="", foreground="#C30E59")
validation_label.grid(row=5, column=0, columnspan=3, sticky="WE", padx=10, pady=5)

window.mainloop()