import tkinter

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
FONT=("Arial,20,italic")


class QuizInterface:
        def __init__(self,Quiz_Brain:QuizBrain):
            self.quiz=Quiz_Brain


            self.window=Tk()
            self.window.title("Quizzler App")
            self.window.config(padx=20,pady=20,bg=THEME_COLOR)

            self.canvas=Canvas()
            self.canvas.config(width=300,height=250)
            self.question_text = self.canvas.create_text(150,125,text="Bu bir deneme",width=200,font=FONT)
            self.canvas.grid(column=0,row=1,columnspan=2)


            self.label_score=Label(text="Score=0",bg=THEME_COLOR,fg="white")
            self.label_score.grid(row=0,column=1,pady=20,padx=20)

            self.photo_right=PhotoImage(file="images\\true.png")
            self.right_button=Button(text="",image=self.photo_right,command=self.is_true)
            self.right_button.config(highlightthickness=0)
            self.right_button.grid(row=2,column=0,padx=20,pady=20)

            self.photo_false = PhotoImage(file="images\\false.png")
            self.false_button = Button(text="", image=self.photo_false,command=self.is_false)
            self.false_button.config(highlightthickness=0)
            self.false_button.grid(row=2, column=1, padx=20, pady=20)


            self.get_next_question()
            self.window.mainloop()

        def get_next_question(self):
            if self.quiz.still_has_questions():
                q_text=self.quiz.next_question()
                self.canvas.itemconfig(self.question_text,text=q_text)
            else:
                self.canvas.itemconfig(self.question_text,text="you are reached end of the game")
                self.false_button.config(state=tkinter.DISABLED)
                self.right_button.config(state=tkinter.DISABLED)
        def is_true(self):
            is_right=self.quiz.check_answer("True")
            self.give_feedback(is_right)



        def is_false(self):
            is_right = self.quiz.check_answer("False")
            self.give_feedback(is_right)


        def give_feedback(self,is_right):
            if is_right=="True":
                self.change_color_is_true()
                self.window.after(1000,self.change_color_to_white)
            if is_right=="False":
                self.change_color_is_false()
                self.window.after(1000, self.change_color_to_white)
            self.get_next_question()
            self.label_score.config(text=f"Score={self.quiz.score}")

        def change_color_is_true(self):
            self.canvas.config(bg="green")
        def change_color_to_white(self):
            self.canvas.config(bg="white")

        def change_color_is_false(self):
            self.canvas.config(bg="red")
