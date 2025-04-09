from tkinter import *
from tkinter import PhotoImage

class CountryQuiz:

    """
    Country Quiz
    """

    def __init__(self):

        image = PhotoImage(file="flag_images/AA-flag.gif")

        self.country_frame = 

        self.country_flag = Label(self.country_frame, image=image)

        self.country_flag.grid(row=1)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Type GUI")
    CountryQuiz()
    root.mainloop()