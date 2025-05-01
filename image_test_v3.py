from tkinter import *
from PIL import Image, ImageTk


class DisplayFlag:
    def __init__(self):
        # Load the image
        self.image = Image.open("AC-flag.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.country_frame = Frame()
        self.country_frame.grid()

        self.country_flag = Label(self.country_frame, image=self.photo)
        self.country_flag.grid()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz Type GUI")
    DisplayFlag()  # Pass root to the class
    root.mainloop()
    