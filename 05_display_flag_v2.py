# Randomly chooses image from csv file
# and displays country flag

from tkinter import *
import csv
from tkinter import Label
from PIL import Image, ImageTk
import random


def get_flags():
    """
    Retrieves flags from csv file
    :return: list of flags which where each list item has the
    country name, associated flag file name and capital name
    """

    file = open("flag_images/country_flags.csv", "r")
    all_flags = list(csv.reader(file, delimiter=","))
    file.close()

    return all_flags

def get_round_flags():
    """
    Choose flag from csv file
    :return: List of flag
    """

    all_flags_list = get_flags()

    potential_flag = random.choice(all_flags_list)

    round_country = (potential_flag[0])
    round_images = potential_flag[3]

    return round_country, round_images


class DisplayFlag:
    """
    Displays flag of the country chosen
    """
    
    def __init__(self):
        # Receives the country and flag chosen
        self.round_country, self.flag_image = get_round_flags()

        # Prints country name for testing
        print(self.round_country)

        # Load the image
        self.image = Image.open(f"flag_images/{self.flag_image}")
        self.image = self.image.resize((210, 150), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.country_frame = Frame(padx=20, pady=10, bg="#FFE1C6")

        self.country_frame.grid()

        self.country_heading = Label(self.country_frame,
                                     text="Country Quiz",
                                     font=("Arial", "18", "bold"), bg="#FFE1C6", width=31)
        self.country_heading.grid(row=0)

        # Create a label to display the image
        self.image_label = Label(self.country_frame, image=self.photo, bg="#FFE1C6")
        self.image_label.grid(row=1)

        # Button to shuffle
        self.next_button = Button(self.country_frame, command=self.next_image, text="Next Flag")
        self.next_button.grid(row=2)

    # Shuffles to different flag
    def next_image(self):
        self.country_frame.destroy()
        DisplayFlag()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Inserting Image")
    app = DisplayFlag()
    root.mainloop()
