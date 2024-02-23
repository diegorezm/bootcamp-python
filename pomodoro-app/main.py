from tkinter import Button, Canvas, Label, PhotoImage, Tk
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1


reps = 0
pomodoros = 0

def clock_display(time: int):
    minutes = math.floor(time / 60)
    seconds = round(time % 60, 2)
    return f"{minutes:02d}:{seconds:02d}"

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global pomodoros
    root.after_cancel(w_timer)
    display = clock_display(WORK_MIN)
    pomodoros_label.config(text="0")
    canvas.itemconfig(timer_text, text=display)
    t.config(text="Work")
    reps = 0
    pomodoros = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global pomodoros
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps > 0 and reps % 2 == 0:
        pomodoros += 1
        pomodoros_label.config(text=pomodoros)
    if reps % 8 == 0:
        t.config(text="Long break",fg=RED)
        timer(long_break_sec)
    elif reps % 2 == 0:
        t.config(text="Short break")
        timer(short_break_sec)
    else:
        t.config(text="Work")
        timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(time: int):
    display = clock_display(time)
    canvas.itemconfig(timer_text, text=display)
    if time > 0:
        global w_timer
        w_timer = root.after(1000, timer,time - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100,pady=50, bg=YELLOW)

t = Label(root, text="Work", bg=YELLOW, fg="#000", font=(FONT_NAME, 35,"bold"))
t.grid(row=1, column=2)


display = clock_display(WORK_MIN)
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112, image=img)
timer_text = canvas.create_text(100,120, text=display,font=(FONT_NAME, 35,"bold"))
canvas.grid(row=2, column=2)

pomodoros_label = Label(root, text=pomodoros, bg=YELLOW, fg="#000", font=(FONT_NAME, 25,"bold"))
pomodoros_label.grid(row=4, column=2)

start_btn = Button(root, text="Start", command=start_timer, bg=GREEN, fg="#000")
start_btn.grid(row=3, column=1)
reset_btn = Button(root, text="Reset", command=reset, bg=RED, fg="#000")
reset_btn.grid(row=3, column=3)

root.mainloop()
