# Second Trial in inserting image...
# Import in code straight from website and it seemed to work

# https://www.geeksforgeeks.org/how-to-add-an-image-in-tkinter/

import tkinter as tk
from tkinter import PhotoImage

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load the image 
image = PhotoImage(file="flag_images/AC-flag.gif")

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()