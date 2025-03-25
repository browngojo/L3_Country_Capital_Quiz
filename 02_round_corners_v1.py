# First trial code for creating rounded buttons....
# The problem was that this code made a oval - shaped button,
# not a rectangle with round corners. But helped me to understand 

from tkinter import *
import tkinter as tk

class CustomButton(tk.Canvas):

    def __init__(self, parent, width, height, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1,
            relief="raised", highlightthickness=0)
        self.command = command

        padding = 4

        # Here is where the button is created using dimensions
        # stated below when the class is called
        id = self.create_oval((padding,padding,
            width+padding, height+padding), outline=color, fill=color)
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


# Main Routine
if __name__ == "__main__":
    app = tk.Tk()
    button = CustomButton(app, 300, 50, "#000000")
    button.pack()
    app.mainloop()