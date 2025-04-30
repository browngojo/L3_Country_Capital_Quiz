# Attempting to insert Image - failed

from tkinter import *
from tkinter import PhotoImage
from PIL import Image

class CountryQuiz:

    """
    Country Quiz
    """

    def __init__(self):

        image = Image.open('flag_images/AA-flag.gif')

        # ... output is created
        self.country_heading = Label(self.country_frame,
                                     text="Country Quiz",
                                     font=("Arial", "18", "bold"), bg="#FFE1C6", width=31)
        self.country_heading.grid(row=0)

        self.country_flag = Label(self.country_frame, image=image)

        self.country_flag.grid(row=1)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Type GUI")
    CountryQuiz()
    root.mainloop()