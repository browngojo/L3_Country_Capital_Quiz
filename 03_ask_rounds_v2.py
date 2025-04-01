from tkinter import *


class AskRounds():
    """
    Asks the user how many rounds they would like to play
    """

    def __init__(self):
        """
        Ask Rounds GUI
        """

        self.round_frame = Frame(padx=10, pady=10, bg="#C7DAFF")

        self.round_frame.grid()

        self.round_heading = Label(self.round_frame, font=("Arial", "15", "bold"), text="Counties & Capitals", bg="#C7DAFF")
        self.round_heading.grid(row=0, pady=10, padx=10)

        self.round_text = Label(self.round_frame, font=("Arial", "11", "normal"), text="Test your geographic knowledge and answer questions correctly. Select the number of rounds you would like to play.", wraplength=350, bg="#C7DAFF")

        self.round_text.grid(row=1, padx=10)

        self.round_error = Label(self.round_frame, font=("Arial", "11", "bold"), bg="#C7DAFF")
        self.round_error.grid(row=2)

        self.round_entry = Entry(self.round_frame, font=("Arial", "14"))
        self.round_entry.grid(row=3, ipadx=2, pady=10, ipady=5)

        # Conversion, help and history / export buttons
        self.enter_button = Button(self.round_frame, font=("Arial", "14"), text="Play", command=self.check_rounds, bg="#2E74FF", width=20)
        self.enter_button.grid(row=4, padx=0, pady=5)

    def check_rounds(self):
        """
        Checks user's input to see if it is an integer
        """
        # Retrieve temperature to be converted
        rounds_wanted = self.round_entry.get()

        # Reset label and entry box (if we had an error)
        self.round_heading.config(fg="#000000", font=("Arial", "15", "bold"))
        self.round_entry.config(bg="#FFFFFF")

        error = "Oops - Please choose a whole number more than zero!"
        has_errors = "no"

        # Checks that amount to be converted is a number above absolute zero
        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                root.withdraw()
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.round_error.config(text=error, fg="#9C0000",
                                      font=("Arial", "10", "bold"))
            self.round_error.grid(row=2, padx=10, pady=10)
            self.round_entry.config(bg="#F4CCCC")
            self.round_entry.delete(0, END)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Ask Rounds GUI")
    AskRounds()
    root.mainloop()
