# Randomly chooses image from csv file
# and displays country flag

from tkinter import *
import csv
from tkinter import Label
from PIL import Image, ImageTk
import random
from functools import partial  # To prevent unwanted windows


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

    round_countries = []

    # loop until we have four colours with different scores...
    while len(round_countries) < 4:
        potential_country = random.choice(all_flags_list)

        # Get the score and check it's not a duplicate
        if potential_country not in round_countries:
            round_countries.append(potential_country)

    round_country = random.choice(round_countries)

    return round_countries, round_country

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

        self.round_heading = Label(self.round_frame, font=("Arial", "15", "bold"), text="Countries & Capitals", bg="#C7DAFF")
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
                CountryQuiz(rounds_wanted)
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


class CountryQuiz:
    """
    Displays flag of the country chosen
    """

    def __init__(self, how_many):
        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_won = IntVar()

        # Colour lists and score list
        self.round_flag_list = []

        self.play_box = Toplevel()

        # If users press the 'x' on the game window, end the entire game!
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        self.photo = ""

        self.country_frame = Frame(self.play_box, padx=20, pady=10, bg="#FFE1C6")

        self.country_frame.grid()

        # Creating the GUI Layout

        self.country_heading = Label(self.country_frame,
                                     text="Country Quiz",
                                     font=("Arial", "18", "bold"), bg="#FFE1C6", width=31)
        self.country_heading.grid(row=0)

        self.round_label = Label(self.country_frame, text="Round # of #", font=("Arial", "16", "bold"), bg="#FFE1C6", wraplength=300, justify="left")

        self.round_label.grid(row=1, pady=10, padx=10)

        self.results_label = Label(self.country_frame, text="You chose, result",
                                   font=("Arial", "12"), bg="#FFE1C6",
                                   wraplength=500, justify="left")

        self.results_label.grid(row=5, pady=10, padx=10)

        # Create a label to display the image
        self.image_label = Label(self.country_frame, image=self.photo, bg="#FFE1C6")
        self.image_label.grid(row=2)

        # set up country button...
        self.button_frame = Frame(self.country_frame, bg="#FFE1C6")
        self.button_frame.grid(row=3)

        self.country_button_ref = []
        self.button_country_list = []

        # create four button in a 1 x 4 grid
        for item in range(0, 4):
            self.country_button = Button(self.button_frame, font=("Arial", "12"),
                                         text="Country Name", width=30,
                                         command=partial(self.round_results, item)
                                         )
            self.country_button.grid(row=item // 2,
                                     column=item % 2,
                                     padx=5, pady=5)
            self.country_button_ref.append(self.country_button)

        # Button to shuffle
        self.next_button = Button(self.country_frame, text="Next Flag",
                                  font=("Arial", "15", "bold"), command=self.new_round, width=29, bg="#2E93FF")
        self.next_button.grid(row=4, pady=10)

        self.end_game_button = Button(self.country_frame, text="End", bg="#E23C3C", command=self.close_game, font=("Arial", "16", "bold"), fg="#FFFFFF", width=21)
        self.end_game_button.grid(row=7, padx=5, pady=5)

        # Once interface has been created, invoke new
        # round function for first round
        self.new_round()

    def new_round(self):
        """
        Chooses four countries and Configures
        buttons with chosen colours
        """

        # Receives the country and flag chosen
        self.round_countries, self.round_country = get_round_flags()

        # Prints country name list for testing
        print(self.round_countries)

        self.round_flag = self.round_country[3]

        # Load the image
        self.image = Image.open(f"flag_images/{self.round_flag}")
        self.image = self.image.resize((210, 150), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label.config(image=self.photo)

        # Retrieve number of rounds played, add one to it and configure heading
        rounds_played = self.rounds_played.get()
        self.rounds_played.set(rounds_played)

        rounds_wanted = self.rounds_wanted.get()

        # Update heading, and score to beat labels. "Hide" results label
        self.round_label.config(text=f"Round {rounds_played + 1} of {rounds_wanted}")
        self.results_label.config(text=f"{'=' * 7}", bg="#FFE1C6")

        # enable country buttons (disabled at the end of the last round)
        for count, item in enumerate(self.country_button_ref):
            item.config(text=self.round_countries[count][0], state=NORMAL)

        self.next_button.config(state=DISABLED)

    def round_results(self, user_choice):
        """
        Retrieves which button was pushed (index 0 - 3), retrieves
        score and then compares it with the median, update results
        and adds results to stats list
        """

        # get user score and colour based on button press...
        # score = int(self.round_[user_choice][1])

        # Add one to the number of rounds played and retrieve
        # the number of rounds won
        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        rounds_won = self.rounds_won.get()

        # alternate way to get button name. Good for if buttons have been scrambled!
        user_choice = self.country_button_ref[user_choice].cget('text')

        round_country = self.round_country[0]

        # retrieve target score and compare with user score to find round result
        # target = self.target_score.get()

        if user_choice == round_country:
            result_text = f"Amazing! {round_country} is correct"
            result_bg = "#82B366"

            rounds_won += 1
            self.rounds_won.set(rounds_won)

        else:
            result_text = f"Oops, it was {round_country}"
            result_bg = "#F8CECC"

        self.results_label.config(text=result_text, bg=result_bg)

        # enable stats & next buttons, disable colour buttons
        self.next_button.config(state=NORMAL)

        # check to see if game is over
        rounds_wanted = self.rounds_wanted.get()

        # Code for when the game ends
        if rounds_played == rounds_wanted:

            # Configure 'end game' labels / buttons
            self.round_label.config(text="Game Over")

            self.next_button.config(state=DISABLED, text="Game Over")

        for item in self.country_button_ref:
            item.config(state=DISABLED)

        # Test if rounds_won working
        print(rounds_won)

    def close_game(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    AskRounds()
    root.mainloop()
