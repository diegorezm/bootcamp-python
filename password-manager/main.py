import tkinter as tk
from tkinter import messagebox
from PassowrdManager import Password, PassowrdManager
import pyperclip

FONT_CONFIG = ("Arial", 14)
HEIGHT = 399
WIDTH = 599

root = tk.Tk()
root.title("Password manager")
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
passwordManager = PassowrdManager()

website = tk.StringVar(root)
emailOrUsername = tk.StringVar(root)
password = tk.StringVar(root)

logo = tk.Canvas(root, width=199, height=224, highlightthickness=0)
img = tk.PhotoImage(file="./logo.png")
logo.create_image(99, 112, image=img)
logo.place(x=199, y=0)

# Labels
default_label_x = 49
default_label_y = 199
website_label = tk.Label(root, text="Website:", font=FONT_CONFIG).place(
    x=default_label_x, y=default_label_y
)
emailOrUsername_label = tk.Label(root, text="Email\\Username:", font=FONT_CONFIG).place(
    x=default_label_x, y=(default_label_y + 39)
)
password_label = tk.Label(root, text="Password:", font=FONT_CONFIG).place(
    x=default_label_x, y=default_label_y + 79
)

# Inputs
default_entry_x = 219
default_entry_y = default_label_y
default_entry_w = 29
website_entry = tk.Entry(root, textvariable=website, width=20).place(
    x=default_entry_x, y=default_entry_y
)
emailOrUsername_entry = tk.Entry(
    root, textvariable=emailOrUsername, width=default_entry_w
).place(x=default_entry_x, y=default_entry_y + 39)

password_entry = tk.Entry(root, textvariable=password, width=20).place(
    x=default_entry_x, y=default_label_y + 79
)


# Btn
def search():
    w = website.get()
    s = passwordManager.search(w)
    if s:
        message = f"email: {s.emailOrUsername}\npassword: {s.password}"
        messagebox.showinfo(title=s.website, message=message)
    else:
        messagebox.showinfo(title="Not found", message="No entry found for this website!")


def random_password():
    password.set(PassowrdManager.gen_random_password())


random_password_btn = tk.Button(
    root, text="random password", width=15, height=1, command=random_password
).place(x=default_entry_x + 160, y=default_entry_y + 79)

search_btn = tk.Button(
    root, text="Search", width=15, height=1, command=search
).place(x=default_entry_x + 160, y=default_entry_y)


def onSubmit():
    newPassword = Password(
        website=website.get(),
        emailOrUsername=emailOrUsername.get(),
        password=password.get(),
    )
    m = f"Password for {newPassword.website} was added!"
    messagebox.showinfo(title="Password added!", message=m)
    pyperclip.copy(newPassword.password)
    passwordManager.create_new_entry(newPassword)


add_new_password = tk.Button(
    root, text="Add", width=default_entry_w, command=onSubmit
).place(x=default_entry_x, y=default_entry_y + 119)

root.mainloop()
