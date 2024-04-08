import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import json

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.root.geometry("400x200")

        self.categories = ["Strategic Management", "Digital Marketing", "Personal Sales", "Information Systems", "Project Management"]
        self.selected_category = tk.StringVar()

        category_label = tk.Label(root, text="Select a category:")
        category_label.pack()

        category_combo = ttk.Combobox(root, textvariable=self.selected_category)
        category_combo['values'] = self.categories
        category_combo.pack()

        start_button = tk.Button(root, text="Start Quiz Now", command=self.start_quiz)
        start_button.pack()

    def start_quiz(self):
        selected_category = self.selected_category.get()
        if not selected_category:
            messagebox.showerror("Error", "Please select a category!")
            return

        self.root.withdraw()  # Hide category selection window
        quiz_window = tk.Toplevel(self.root)
        QuizWindow(quiz_window, selected_category)

class QuizWindow:
    def __init__(self, root, category):
        self.root = root
        self.root.title("Quiz - " + category)
        self.root.geometry("600x400")

        self.questions = self.load_questions(category)
        self.current_question_index = 0
        self.selected_answer = tk.StringVar()

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.selected_answer, value=str(i+1))
            self.option_buttons.append(button)
            button.pack()

        submit_button = tk.Button(root, text="Submit Answer", command=self.submit_answer)
        submit_button.pack()

        self.display_question()

    def load_questions(self, category):
        print("Selected category:", category)  # Debugging statement
        conn = sqlite3.connect('quiz_questions.db')
        c = conn.cursor()

    # Print the SQL query being executed
        sql_query = "SELECT question, options, correct_answer FROM questions WHERE category=?"
        print("SQL Query:", sql_query)  # Debugging statement

    # Query questions for the given category from the database
        c.execute(sql_query, (category,))
        questions_data = c.fetchall()

        print("Number of questions retrieved:", len(questions_data))  # Debugging statement

    # Convert database rows into Question objects
        questions = []
        for question_data in questions_data:
            question = Question(question_data[0], json.loads(question_data[1]), question_data[2])
            questions.append(question)

        conn.close()
        return questions


    def display_question(self):
        print("Current question index:", self.current_question_index)
        print("Total number of questions:", len(self.questions))
    
        if self.current_question_index < 10:  # Check if less than 10 questions have been asked
            if self.current_question_index < len(self.questions):
                question = self.questions[self.current_question_index]
                print("Displaying question:", question.question)
                self.question_label.config(text=question.question)
                for i, option in enumerate(question.options):
                    self.option_buttons[i].config(text=option)
                self.selected_answer.set("")
        else:
            print("Quiz completed")
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            return  # End the function here to prevent further questions from being displayed



    def submit_answer(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            user_answer_index = int(self.selected_answer.get()) - 1  # Convert selected answer to index
            correct_answer_index = ord(question.correct_answer) - ord('A')  # Convert correct answer to index
            if user_answer_index == correct_answer_index:
                messagebox.showinfo("Correct", "Your answer is correct!")
            else:
                messagebox.showinfo("Incorrect", "Your answer is incorrect. The correct answer is " + question.correct_answer)
            self.current_question_index += 1
            self.display_question()




root = tk.Tk()
app = QuizGUI(root)
root.mainloop()
