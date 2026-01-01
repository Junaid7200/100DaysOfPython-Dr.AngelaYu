THEME_COLOR = "#375362"

import tkinter as tk


from quiz_brain import QuizBrain
class QuizInterface: 
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="yoyoyoyo", font=("Ariel", 20, "italic"))
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 50) 
        self.true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=self.true_image, highlightthickness=0, bg="green", fg="white", command=self.check_true)
        self.true_button.grid(row=2, column=0)
        self.false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=self.false_image, highlightthickness=0, bg="red", fg="white", command=self.check_false)
        self.false_button.grid(row=2, column=1)
        
        
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self, user_answer="true"):
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def check_false(self, user_answer="false"):
        is_false = self.quiz.check_answer(user_answer)
        self.give_feedback(is_false)
    
    def give_feedback(self, param):
        if param:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)