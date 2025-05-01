# First Trial in inserting image... - failed

from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


class DisplayFlag:

    def __init__(self):
        # One flag for testing
        img = PhotoImage(file="AC-flag.png")

        self.country_frame = Frame()
        self.country_frame.grid()

        self.country_flag = Label(self.country_frame, image=img)
        self.country_flag.grid(row=0)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Type GUI")
    DisplayFlag()
    root.mainloop()
