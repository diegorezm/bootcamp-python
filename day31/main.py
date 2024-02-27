import tkinter as tk
from load_data import french_wordlist, data,get_indexes, save
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
HEIGHT = 900
WIDTH = 1200
FONT_TITLE = ("Arial", 35, 'italic')
FONT = ("Arial", 40, "bold")
right_indexes = get_indexes()
french_index = 0
while french_index < len(french_wordlist) and french_index in right_indexes:
    french_index += 1
french_wordlist = french_wordlist.tolist()

root = tk.Tk()
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
root.configure(bg=BACKGROUND_COLOR)

def to_french():
    global french_index,flip_timer
    root.after_cancel(flip_timer)
    if french_index < len(french_wordlist):
        card_c.itemconfigure(card_text, text=french_wordlist[french_index], fill="#000")
        card_c.itemconfigure(card_title, text="French", fill="#000")
        card_c.itemconfigure(card_c_img, image=card_front_img)
        flip_timer = root.after(3000, to_english)
    else:
        messagebox.showinfo(title="End", message="You have completed the game!")

def swap_card():
    global french_index
    while french_index < len(french_wordlist) and french_index + 1 in right_indexes:
        french_index += 1
    else:
        french_index += 1
    to_french()

def swap_right():
    if french_index < len(french_wordlist):
        right_indexes.append(french_index)
        save(right_indexes)
        swap_card()
    else:
        messagebox.showinfo(title="End", message="You have completed the game!")

def to_english():
    global french_index
    word = french_wordlist[french_index]
    english_word = data[word]
    card_c.itemconfigure(card_text, text=english_word, fill="#fff")
    card_c.itemconfigure(card_title, text="English", fill="#fff")
    card_c.itemconfigure(card_c_img, image=card_back_img)

flip_timer = root.after(3000,to_english)

card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_back_img = tk.PhotoImage(file="./images/card_back.png")
card_c = tk.Canvas(root, width=850, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
card_c_img = card_c.create_image(450,300,image=card_front_img)
card_c.place(x=150,y=80)
card_title = card_c.create_text(450,100, text="French", font=FONT_TITLE)
card_text = card_c.create_text(450,300, text=french_wordlist[french_index], font=FONT)

# btn

x_img = tk.PhotoImage(file="./images/wrong.png")
v_img = tk.PhotoImage(file="./images/right.png")

btn_x = 300
btn_y = 700

x_btn = tk.Button(root, image=x_img, borderwidth=0, command=swap_card)
x_btn.place(x=btn_x, y=btn_y)
v_btn = tk.Button(root, image=v_img, borderwidth=0, command=swap_right)
v_btn.place(x=btn_x + 450, y=btn_y)

root.mainloop()
