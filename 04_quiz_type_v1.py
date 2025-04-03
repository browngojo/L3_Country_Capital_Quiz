# First iteration of Quiz Type GUI
# Everything works fine

from tkinter import *


class QuizType:
    """
    Choose Type of Quiz
    """

    def __init__(self):

        self.welcome_frame = Frame(padx=20, pady=10, bg="#FED9B7")
        self.root = None

        self.welcome_frame.grid()

        # Heading Text
        self.welcome_heading = Label(self.welcome_frame,
                                     text="Please choose a Quiz Category",
                                     font=("Arial", "18", "bold"), bg="#FED9B7", width=31)
        self.welcome_heading.grid(row=0)

        self.button_frame = Frame(padx=20, pady=10, bg="#FED9B7")
        self.button_frame.grid(row=1)

        # Country Quiz Button
        self.country_button = Button(self.button_frame,
                                     text="Country Quiz (Easy)",
                                     font=("Arial", "12", "bold"), bg="#81A4CD", fg="white", width=20,
                                     command=self.to_countryquiz)
        self.country_button.grid(row=1, column=0, padx=5, ipady=10, ipadx=8)

        # Capital Quiz Button
        self.capital_button = Button(self.button_frame,
                                     text="Capital Quiz (Hard)", font=("Arial", "12", "bold"),
                                     bg="#FF6978", fg="white", width=20, command=self.to_capitalquiz)
        self.capital_button.grid(row=1, column=1, padx=5, ipady=10, ipadx=8)

    # .... closes Quiz Type

    def to_countryquiz(self):
        # Deletes the frames
        self.welcome_frame.destroy()
        self.button_frame.destroy()
        # Calls Country Quiz
        CountryQuiz()

    def to_capitalquiz(self):
        # Deletes the frames
        self.welcome_frame.destroy()
        self.button_frame.destroy()
        # Calls Country Quiz
        CapitalQuiz()


class CountryQuiz:

    """
    Country Quiz
    """

    def __init__(self):
        self.country_frame = Frame(padx=20, pady=10, bg="#FED9B7")

        self.country_frame.grid()

        # Heading Text
        self.country_heading = Label(self.country_frame,
                                     text="Country Quiz",
                                     font=("Arial", "18", "bold"), bg="#FED9B7", width=31)
        self.country_heading.grid(row=0)


class CapitalQuiz:

    """
    Capital Quiz
    """

    def __init__(self):
        self.capital_frame = Frame(padx=20, pady=10, bg="#FED9B7")

        self.capital_frame.grid()

        # Heading Text
        self.capital_heading = Label(self.capital_frame,
                                     text="Capital Quiz",
                                     font=("Arial", "18", "bold"), bg="#FED9B7", width=31)
        self.capital_heading.grid(row=0)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Type GUI")
    QuizType()
    root.mainloop()
