from tkinter import *
from functools import partial # To prevent unwanted windows

class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self):

        self.game_frame = Frame()
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame,
                                   text="Capital Country Quiz",
                                   font=("Arial", "16", "bold"), padx=5, pady=5)
        self.heading_label.grid(row=0)

        self.hints_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="Hints", width=15, fg="#FFFFFF",
                                   bg="#FF8000", padx=10, pady=10, command=self.to_hints)
        self.hints_button.grid(row=1)

    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        DisplayHints(self)
        root.withdraw()

class DisplayHints:

    def __init__(self, partner):

        # Setup dialogue box and background colour
        background = "#d7c1e2"
        self.help_box = Toplevel()

        # Disable help button
        #partner.stats_button.config(state=DISABLED)

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info", font=("Arial", "16", "bold"))
        self.help_heading_label.grid(row=0, pady=7)

        help_text = "Welcome to Countries and Capitals Quiz!\n\nThis quiz is made to test your knowledge and in each round you are given a question such as 'What is the Capital of New Zealand?' and you will be given 4 options to choose from. " \
                    "\n\nOnce you have chosen an option, click the 'Next Round' Button to move on. If you would like to view how well you did, you can click the 'Stats' Button from which you can also export a file with the stats.\n\nEnjoy the Quiz and all the best!"

        print("hello")
        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Close", bg="#A680B8", width=10,
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal...
        partner.hints_button.config(state=NORMAL)
        self.help_box.destroy()
        root.deiconify()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Help / Info GUI Testing")
    Play()
    root.mainloop()