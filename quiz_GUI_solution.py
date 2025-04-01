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
              "options": ["Greek", "Russian", "Arabic", "Japanese"],
              "answer": "Russian"},
            
            {"question": "Which of the following languages has the longest alphabet?",
              "options": ["Greek", "Russian", "Arabic", "Japanese"],
              "answer": "Russian"},
            
            {"question": "Which of the following languages has the longest alphabet?",
              "options": ["Greek", "Russian", "Arabic", "Japanese"],
              "answer": "Russian"},
            
            { "question": "Which of the following languages has the longest alphabet?",
              "options": ["Greek", "Russian", "Arabic", "Japanese"],
              "answer": "Russian"}]

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
            radio_button = Radiobutton(self.options_frame, text="", variable=self.selected_option, value="", command=self.next_question)
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        #frame & label for right or wrong answer
        self.feedback_frame = Frame(self.root)
        self.feedback_frame.pack()

        self.feedback_label = Label(self.feedback_frame, text="")
        self.feedback_label.pack()

        #next button
        self.next_button = Button(self.root, text="Next", command=self.next_question, state=DISABLED)
        self.next_button.pack()
        
        #automatically display first question when program is opened
        self.display_question()

    #display the question - showing the current question to the user
    def display_question(self):
        """Display current question with answer options for the user"""
        question_info = self.questions[self.current_question]
        self.question_label.config(text=question_info["question"])

        #update and populate radiobuttons with option values
        self.radio_buttons[0].config(text=question_info["options"][0], value=question_info["options"][0])
        self.radio_buttons[1].config(text=question_info["options"][1], value=question_info["options"][1])
        self.radio_buttons[2].config(text=question_info["options"][2], value=question_info["options"][2])
        self.radio_buttons[3].config(text=question_info["options"][3], value=question_info["options"][3])

        #set first radiobutton as default selection
        self.selected_option.set(question_info["options"][0])

        #enable next button
        self.next_button.config(state=NORMAL)
        
        
    def next_question(self):
        """handle next button click"""
        selected_answer = self.selected_option.get()
        correct_answer = self.questions[self.current_question]["answer"]

        #checking if selected answer matches correct answer
        if selected_answer == correct_answer:
            self.score =+ 1 #update score accordingly
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Wrong!", fg="red")
            

        #move to next question
        self.current_question += 1

        #if there are still questions left then should display next question
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_score() #if it is last question, it should display final score


    def show_score(self):
        """Display the users final score"""
        self.question_label.config(text=f"Your final score: {self.score}/{len(self.questions)}")

        #hide all widgets not needed
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()
            
        self.next_button.pack_forget()
        self.feedback_label.config(text="") #will clear last feedback msg
            
                
#main app window - run program            
root = Tk()
quiz_app = Quiz(root)
root.mainloop()
