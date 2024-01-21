from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Pergunta teste", fill=THEME_COLOR, font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label_score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg=WHITE)
        self.label_score.grid(row=0, column=1)

        true_image = PhotoImage(file="./Day 34 - Quizzler API/images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.pressed_true)
        self.button_true.grid(row=2, column=0)

        false_image = PhotoImage(file="./Day 34 - Quizzler API/images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.pressed_false)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")
            
        self.canvas.config(bg=WHITE)

    def pressed_true(self):
        result = self.quiz.check_answer("true")
        self.give_feedback(result)

    def pressed_false(self):
        result = self.quiz.check_answer("false")
        self.give_feedback(result)

    def give_feedback(self, result):

        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
