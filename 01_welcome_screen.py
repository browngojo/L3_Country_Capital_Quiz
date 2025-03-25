from tkinter import *

class Welcome():
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



    def __init__(self):

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

        # Button when clicked.....
        self.next_button = Button(self.welcome_frame,
                                  text="Next", font=("Arial", "18", "bold"),
                                  bg="#76A333", fg="white", command=self.to_askrounds, width=20)
        self.next_button.grid(row=2, padx=0, pady=5)

    # .... closes welcome screen (will soon link to the next GUI)
    def to_askrounds(self):
        root.withdraw()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country-Capital Quiz")
    Welcome()
    root.mainloop()
