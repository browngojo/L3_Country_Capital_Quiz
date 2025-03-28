# Failed trialling, trying to integrate code from 02_round_corners_v3.py

from tkinter import *
import tkinter as tk


class Welcome(tk.Canvas):
    """
    Welcome Screen for the User
    """

    # Body text
    information_text = ("Hey there, User! This quiz tests you on your knowledge of Countries by looking at their "
                        "respective flags and Capitals of various Countries.\n\nBy clicking the button below, you "
                        "will have to enter the amount of rounds you would like to play. Once chosen, you will "
                        "then have to choose either Country Quiz (Easy) or Capital Quiz (Hard).\n\nFrom there on, "
                        "the quiz will begin. If you would like to view how well you did, you can click the "
                        "'Stats' Button from you can also export a file with the stats.\n\nEnjoy yourself "
                        "and all the best!")

    def __init__(self, master=None, text: str = "", radius=10, btnforeground="#C2E292",     btnbackground="#C2E292", clicked=None, *args, **kwargs):

        self.welcome_frame = Frame(padx=20, pady=10, bg="#C2E292")
  
        self.welcome_frame.grid()

        # Heading Text
        self.welcome_heading = Label(self.welcome_frame,
                                     text="Welcome to the Country-Capital Quiz!",
                                     font=("Arial", "16", "bold"), bg="#C2E292"
                                     )
        self.welcome_heading.grid(row=0)

        # Body Text
        self.welcome_text = Label(self.welcome_frame,
                                  text=self.information_text, justify="left", wraplength=450,
                                  font=("Arial", "11", "normal"), bg="#C2E292"
                                  )
        self.welcome_text.grid(row=1, pady=5, padx=0)

        # Button Creation...
        super(Welcome, self).__init__(master, *args, **kwargs)
        self.config(bg=self.master["bg"])
        self.btnbackground = btnbackground
        self.clicked = clicked

        self.radius = radius

        self.rect = self.round_rectangle(0, 0, 0, 0, tags="button", radius=radius, fill=btnbackground)
        self.text = self.create_text(0, 0, text=text, tags="button", fill=btnforeground, font=("Arial", 16, "bold"),
                                     justify="center")

        self.tag_bind("button", "<ButtonPress>", self.border)
        self.tag_bind("button", "<ButtonRelease>", self.border)
        self.bind("<Configure>", self.resize)

        text_rect = self.bbox(self.text)
        if int(self["width"]) < text_rect[2] - text_rect[0]:
            self["width"] = (text_rect[2] - text_rect[0]) + 10

        if int(self["height"]) < text_rect[3] - text_rect[1]:
            self["height"] = (text_rect[3] - text_rect[1]) + 10

    def round_rectangle(self, x1, y1, x2, y2, radius=10, update=False, **kwargs):
        # if update is False a new rounded rectangle's id will be returned else updates existing rounded rect.
        # source: https://stackoverflow.com/a/44100075/15993687
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        if not update:
            return self.create_polygon(points, **kwargs, smooth=True)

        else:
            self.coords(self.rect, points)

    def resize(self, event):
        event.width = 200
        event.height = 100

        text_bbox = self.bbox(self.text)

        if self.radius > event.width or self.radius > event.height:
            radius = min((event.width, event.height))

        else:
            radius = self.radius

        if event.width < text_bbox[2] - text_bbox[0]:
            event.width = text_bbox[2] - text_bbox[0] + 30

        if event.height < text_bbox[3] - text_bbox[1]:
            event.height = text_bbox[3] - text_bbox[1] + 30

        self.round_rectangle(5, 5, event.width - 5, event.height - 5, radius, update=True)

        bbox = self.bbox(self.rect)

        x = ((bbox[2] - bbox[0]) / 2) - ((text_bbox[2] - text_bbox[0]) / 2)
        y = ((bbox[3] - bbox[1]) / 2) - ((text_bbox[3] - text_bbox[1]) / 2)

        self.moveto(self.text, x, y)

    def border(self, event):
        if event.type == "4":
            self.itemconfig(self.rect, fill="#d2d6d3")
            if self.clicked is not None:
                self.clicked()

        else:
            self.itemconfig(self.rect, fill=self.btnbackground)

    # .... closes welcome screen (will soon link to the next GUI)
    def to_askrounds(self):
        root.withdraw()


def func():
    print("Button pressed")


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country-Capital Quiz")
    btn = Welcome(text="This is a \n rounded button", radius=30, btnbackground="#76A333",
                        btnforeground="#ffffff", clicked=func)
    btn.grid(padx=5, pady=5)
    root.mainloop()
