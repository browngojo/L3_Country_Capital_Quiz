# https://www.geeksforgeeks.org/how-to-add-an-image-in-tkinter/

from tkinter import *
from tkinter import Label
from PIL import Image, ImageTk


class DisplayFlag:
    def __init__(self):
        # Load the image
        self.image = Image.open("flag_images/AC-flag.gif")
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a label to display the image
        self.image_label = Label(image=self.photo)
        self.image_label.pack()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Inserting Image")
    app = DisplayFlag()
    root.mainloop()
