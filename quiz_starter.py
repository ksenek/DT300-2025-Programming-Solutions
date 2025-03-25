#quizGUI.py

from tkinter import *


class Quiz:
    def __init__(self, root):
        self.root=root
        self.root.title("Miss Senek's Fun Quiz")
        self.root.geometry("400x300")

        #list of questions with answers/options
        self.questions = [
            { "question": "What is the capital of France?",
              "options": ["Paris", "London", "Tokyo", "Berlin"],
              "answer": "Paris"},

            { "question": "Which of the following languages has the longest alphabet?",
              "options": ["Greek", "Russian", "Arabic", "Japanese"]
              "answer": "Russian"} ]

        self.current_question = 0 #start at first question
        self.score = 0 #set starting score to 0

        #frame for questions
        self.question_frame = Frame(self.root) 
        self.question_frame.pack()

        #label for questions to be populated by dictionary info
        self.question_label = Label(self.question_frame, text="")
        self.question_label.pack()

        #options with radiobuttons
        self.options_frame = Frame(self.root)
        self.options_frame.pack()

        self.selected_option = StringVar()
        self.radio_buttons = []
        #for loop to iterate over options to create manually
        for i in range(4):
            radio_button = Radiobutton(self.options_frame, text="", variable=self.selected_option, value="", command=)
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        #label for right or wrong answer

        #next button

        #display the question - function!
            


        

        

            
            
        



root = Tk()
root.mainloop()
