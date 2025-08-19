import tkinter as tk
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        # Load Images 
        self.right_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")

        # Create Canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(
            150, 125, text="Some Quest", width=270,
            font=("Arial", 20, "italic"), fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Score Label
        self.score = tk.Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",10,"bold"))
        self.score.grid(row=0, column=1)

        # Buttons
        self.right_button = tk.Button(image=self.right_img, highlightthickness=0, bd=0)
        self.right_button.grid(row=3, column=1, pady=10)
        self.wrong_button = tk.Button(image=self.wrong_img, highlightthickness=0, bd=0)
        self.wrong_button.grid(row=3, column=0, pady=10)

        self.get_next_question()
        self.root.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=q_text)
