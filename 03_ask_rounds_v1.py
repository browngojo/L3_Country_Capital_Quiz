from tkinter import *


class AskRounds():
    """
    Asks the user how many rounds they would like to play
    """

    def __init__(self):
        """
        Ask Rounds GUI
        """

        self.round_frame = Frame(padx=10, pady=10)
        self.round_frame.grid()

        self.round_label = Label(self.round_frame, font=("Arial", "11", "bold"), text="How many rounds would you like to play?")
        self.round_label.grid(row=0, pady=10, padx=10)

        self.round_entry = Entry(self.round_frame,
                                 font=("Arial", "14")
                                 )
        self.round_entry.grid(row=1, padx=10, pady=10)

        # Conversion, help and history / export buttons
        self.enter_button = Button(self.round_frame, font=("Arial", "14"), text="Enter", command=self.check_rounds)
        self.enter_button.grid(row=2)

    def check_rounds(self):
        """
        Checks user's input to see if it is an integer
        """
        # Retrieve temperature to be converted
        rounds_wanted = self.round_entry.get()

        # Reset label and entry box (if we had an error)
        self.round_label.config(fg="#000000", font=("Arial", "12", "bold"))
        self.round_entry.config(bg="#FFFFFF")

        error = "Oops - Please choose a whole number more than zero!"
        has_errors = "no"

        # Checks that amount to be converted is a number above absolute zero
        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                self.round_label.config(fg="#009900", font=("Arial", "14", "bold"), text=f"You chose {rounds_wanted} round(s)")
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.round_label.config(text=error, fg="#990000",
                                     font=("Arial", "10", "bold"))
            self.round_entry.config(bg="#F4CCCC")
            self.round_entry.delete(0, END)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Check Rounds Testing")
    AskRounds()
    root.mainloop()
