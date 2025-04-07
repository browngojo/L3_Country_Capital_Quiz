# Second iteration of Quiz Type GUI
# More efficient code

from tkinter import *


class QuizType:
    """
    Choose Type of Quiz
    """

    def __init__(self):
        self.welcome_frame = Frame(padx=20, pady=10, bg="#FFE1C6")
        self.root = None

        self.welcome_frame.grid()

        # Heading Text
        self.welcome_heading = Label(self.welcome_frame,
                                     text="Please choose a Quiz Category",
                                     font=("Arial", "18", "bold"), bg="#FFE1C6", width=31)
        self.welcome_heading.grid(row=0)

        self.button_frame = Frame(padx=20, pady=10, bg="#FFE1C6")
        self.button_frame.grid(row=1)

        # Button List
        quiz_button_list = [
            [self.button_frame, "Country Quiz (Easy)", "#81A4CD", lambda: self.to_quiz("country"), 0],
            [self.button_frame, "Capital Quiz (Hard)", "#FF6978", lambda: self.to_quiz("capital"), 1]
        ]

        # Creates buttons using the list above
        button_ref_list = []
        for item in quiz_button_list:
            make_control_button = Button(item[0], text=item[1], bg=item[2],
                                         command=item[3], font=("Arial", "12", "bold"), fg="white", width=20)
            make_control_button.grid(row=0, column=item[4], padx=5, ipady=10, ipadx=8)

            button_ref_list.append(make_control_button)

        # Retrieves the buttons
        self.country_button = button_ref_list[0]
        self.capital_button = button_ref_list[1]

    def to_quiz(self, quiz_type):
        # Deletes frames
        self.welcome_frame.destroy()
        self.button_frame.destroy()
        # Calls Quiz
        Quiz(quiz_type)


class Quiz:
    """
    Both of the Quizzes
    """

    def __init__(self, quiz_type):
        self.country_frame = Frame(padx=20, pady=10, bg="#FFE1C6")

        self.country_frame.grid()

        # Depending on the button clicked...
        if quiz_type == "country":
            quiz_heading = "Country Quiz"

        else:
            quiz_heading = "Capital Quiz"

        # ... output is created
        self.country_heading = Label(self.country_frame,
                                     text=quiz_heading,
                                     font=("Arial", "18", "bold"), bg="#FFE1C6", width=31)
        self.country_heading.grid(row=0)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Type GUI")
    QuizType()
    root.mainloop()
