from time import sleep
from tkinter import Button, Canvas, Label, Tk, PhotoImage
from quiz_brain import QuizBrain

from question_model import Question

THEME_COLOR = "#375362"
FONT = ("Arial", 30, "bold")


class UI(Tk):
    def __init__(
        self,
        q: list[Question],
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Quiz App")
        self.geometry("800x900")
        self.configure(bg=THEME_COLOR)
        self.q = q
        self.score = 0
        self.scoreboard = Label(self,text=f"score: {self.score}", bg=THEME_COLOR, fg="#fff",font=FONT)
        self.scoreboard.place(x=550,y=50)
        self.current_question = q[0]
        self.quizBrain = QuizBrain(q)
        self.false_btn_img = PhotoImage(file="./images/false.png")
        self.true_btn_img = PhotoImage(file="./images/true.png")
        self.btn_x = 100
        self.btn_y = 650
        self.canvas = Canvas(self, bg="#fff", width=600, height=500)
        self.canvas.place(x=100, y=100)
        self.canvas_text = self.canvas.create_text(
            300,
            100,
            text=self.current_question.question,
            font=FONT,
            anchor="n",
            justify="center",
            width=500,
        )
        self.btn_false = Button(self, image=self.false_btn_img, borderwidth=0, command=lambda: self.set_user_answer(False))
        self.btn_false.place(x=self.btn_x, y=self.btn_y)
        self.btn_true = Button(self, image=self.true_btn_img, borderwidth=0,command=lambda: self.set_user_answer(True))
        self.btn_true.place(x=self.btn_x + 500, y=self.btn_y)

    def next_question(self):
        nq = self.quizBrain.next_question()
        self.canvas.configure(bg="#fff")
        if nq != None:
            self.canvas.itemconfigure(self.canvas_text, text=nq.question)
            self.current_question = nq
        else:
            self.canvas.itemconfigure(self.canvas_text, text="No more questions to display!")

    def set_user_answer(self,u: bool):
        answ = self.quizBrain.check_answer(u)
        if answ:
            self.canvas.configure(bg="green")
            self.score += 1
            self.scoreboard.configure(text=f"score: {self.score}")
        else:
            self.canvas.configure(bg="red")
        self.update()
        sleep(1)
        self.next_question()
