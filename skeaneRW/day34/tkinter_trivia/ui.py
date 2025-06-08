import tkinter as tk
from html import unescape
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface(QuizBrain):
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.canvas = tk.Canvas(width= 300,height=250, bg="white")
        self.quiz_question = self.canvas.create_text(150,125,text=unescape(self.current_question["text"]), width=280, font=("Arial", 16, "bold"))
        true_image = tk.PhotoImage(file="skeaneRW/day34/tkinter_trivia/images/true.png")
        false_image = tk.PhotoImage(file="skeaneRW/day34/tkinter_trivia/images/false.png")
        self.true_btn = tk.Button(image=true_image, highlightthickness=0, command=lambda: check_answer(self, True))
        self.false_btn = tk.Button(image=false_image, highlightthickness=0, command=lambda: check_answer(self, False))
        
        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true_btn.grid(row=2, column=0, pady=10)
        self.false_btn.grid(row=2, column=1, pady=10)

        def check_answer(self, bool:bool):
            correct_answer = self.current_question["answer"]
            is_correct = self.check_user_response(str(bool),correct_answer)
            if is_correct:
                self.canvas.config(bg="#A1EEBD")
                self.score_label.config(text=f"score: {self.score}")
            else:
                self.canvas.config(bg="#F6D6D6")
            self.canvas.after(400, lambda: get_next_question(self))
            return

        def get_next_question(self) -> None:
            self.canvas.config(bg="white")
            if not self.is_over():
                self.next_question()
                next_question = unescape(self.current_question["text"])
                self.canvas.itemconfig(self.quiz_question, text=next_question)

        self.window.mainloop()