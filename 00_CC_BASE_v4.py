# V4 of Entire Capital & Country QUIZ
# This one includes the two quizzes and the


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

    # remove the first row
    all_flags.pop(0)

    return all_flags


def get_round_flags():
    """
    Choose flag from csv file
    :return: List of flag
    """

    all_flags_list = get_flags()

    round_countries = []

    # loop until we have four countries' data...
    while len(round_countries) < 4:
        potential_country = random.choice(all_flags_list)

        # Get the score and check it's not a duplicate
        if potential_country not in round_countries:
            round_countries.append(potential_country)

    round_country = random.choice(round_countries)

    return round_countries, round_country



class Welcome:
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
        # Setup dialogue box and background colour
        background = "#C2E292"

        self.welcome_frame = Frame(padx=20, pady=10)

        self.welcome_frame.grid()

        # Heading Text
        self.welcome_heading = Label(self.welcome_frame,
                                     text="Welcome to the Country-Capital Quiz!",
                                     font=("Arial", "16", "bold"))
        self.welcome_heading.grid(row=0)

        # Body Text
        self.welcome_text = Label(self.welcome_frame,
                                  text=self.information_text, justify="left", wraplength=450,
                                  font=("Arial", "11", "normal"))
        self.welcome_text.grid(row=1, pady=5, padx=0)

        # Button when clicked.....
        self.next_button = Button(self.welcome_frame,
                                  text="Next", font=("Arial", "15", "bold"),
                                  bg="#76A333", fg="white", command=self.to_askrounds, width=18)
        self.next_button.grid(row=2, padx=0, pady=5)

        # List and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.welcome_frame, self.welcome_heading, self.welcome_text]

        for item in recolour_list:
            item.config(bg=background)

    # .... closes welcome screen (will soon link to the next GUI)
    def to_askrounds(self):
        # Calls Ask Round GUI
        AskRounds()
        # Closes Welcome GUI
        root.withdraw()


class AskRounds:
    """
    Asks the user how many rounds they would like to play
    """

    def __init__(self):
        """
        Ask Rounds GUI
        """

        # Setup dialogue box and background colour
        background = "#C7DAFF"

        self.play_box = Toplevel()

        # If users press the 'x' on the game window, end the entire game!
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        self.round_frame = Frame(self.play_box, padx=10, pady=10)

        self.round_frame.grid()

        self.round_heading = Label(self.round_frame, font=("Arial", "15", "bold"),
                                   text="Countries & Capitals")
        self.round_heading.grid(row=0, pady=10, padx=10)

        self.round_text = Label(self.round_frame, font=("Arial", "11", "normal"),
                                text="Test your geographic knowledge and answer questions correctly. "
                                     "Select the number of rounds you would like to play.",
                                wraplength=350)

        self.round_text.grid(row=1, padx=10)

        self.round_error = Label(self.round_frame, font=("Arial", "11", "bold"))
        self.round_error.grid(row=2)

        self.round_entry = Entry(self.round_frame, font=("Arial", "14"))
        self.round_entry.grid(row=3, ipadx=2, pady=10, ipady=5)

        # Conversion, help and history / export buttons
        self.enter_button = Button(self.round_frame, font=("Arial", "15", "bold"), text="Play", fg="white",
                                   command=self.check_rounds, bg="#2E74FF", width=18)
        self.enter_button.grid(row=4, padx=0, pady=5)

        # List and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.round_frame, self.round_heading, self.round_text, self.round_error]

        for item in recolour_list:
            item.config(bg=background)

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
                self.to_quiztype(rounds_wanted)

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

    def to_quiztype(self, rounds_wanted):
        # Closes Ask Rounds GUI
        self.play_box.destroy()
        # Calls Quiz Type GUI
        QuizType(rounds_wanted)


class QuizType:
    """
    Choose Type of Quiz
    """

    def __init__(self, rounds_wanted):
        # Setup dialogue box and background colour
        background = "#FFE1C6"

        self.play_box = Toplevel()

        # If users press the 'x' on the game window, end the entire game!
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        self.quiztype_frame = Frame(self.play_box, padx=20, pady=10)

        self.quiztype_frame.grid()

        # Heading Text
        self.quiztype_heading = Label(self.quiztype_frame,
                                     text="Please choose a Quiz Category",
                                     font=("Arial", "18", "bold"), width=31)
        self.quiztype_heading.grid(row=0)

        self.button_frame = Frame(self.play_box, padx=20, pady=10)
        self.button_frame.grid(row=1)

        # Button List
        quiz_button_list = [
            [self.button_frame, "Country Quiz (Easy)", "#81A4CD", lambda: self.to_quiz("Country", rounds_wanted), 0],
            [self.button_frame, "Capital Quiz (Hard)", "#FF6978", lambda: self.to_quiz("Capital", rounds_wanted), 1]
        ]

        # Creates buttons using the list above
        button_ref_list = []
        for item in quiz_button_list:
            make_control_button = Button(item[0], text=item[1], bg=item[2],
                                         command=item[3], font=("Arial", "12", "bold"), fg="white", width=20)
            make_control_button.grid(row=0, column=item[4], padx=5, ipady=10, ipadx=8)

            button_ref_list.append(make_control_button)

        # Retrieves the buttons
        self.country_button = button_ref_list[0]
        self.capital_button = button_ref_list[1]

        # List and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.quiztype_frame, self.quiztype_heading, self.button_frame]

        for item in recolour_list:
            item.config(bg=background)

    def to_quiz(self, quiz_type, rounds_wanted):
        # Deletes frames
        self.play_box.destroy()
        CountryCapitalQuiz(rounds_wanted, quiz_type)


class CountryCapitalQuiz:
    """
    Set up the Country Capital GUI, in which, depending on the type of quiz
    chosen by user, the GUI will output a quiz for either Countries or Capitals
    """

    def __init__(self, how_many, quiz_type):
        # Setup dialogue box and background colour
        background = "#FFE1C6"

        self.quiztype = quiz_type
        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_won = IntVar()

        # Flag list
        self.round_flag_list = []

        self.play_box = Toplevel()

        # If users press the 'x' on the game window, end the entire game!
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        self.photo = ""

        self.quiz_frame = Frame(self.play_box, padx=20, pady=10)

        self.quiz_frame.grid()

        # Creating the GUI Layout

        self.quiz_heading = Label(self.quiz_frame,
                                     text=f"{quiz_type} Quiz",
                                     font=("Arial", "18", "bold"), width=31)
        self.quiz_heading.grid(row=0)

        # Round heading
        self.round_label = Label(self.quiz_frame, text="Round # of #", font=("Arial", "16", "bold"), wraplength=300, justify="left")

        self.round_label.grid(row=1, pady=10, padx=10)

        # Update heading, and score to beat labels. "Hide" results label
        self.round_heading = Label(self.quiz_frame, text="question",
                                   font=("Arial", "15", "bold"))
        self.round_heading.grid(row=2)

        self.results_label = Label(self.quiz_frame, text="You chose, result",
                                   font=("Arial", "12"),
                                   wraplength=500, justify="left")

        self.results_label.grid(row=5, pady=10, padx=10)

        # Create a label to display the image
        self.image_label = Label(self.quiz_frame, image=self.photo)
        self.image_label.grid(row=3)

        # set up country button...
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        self.quiz_button_ref = []
        self.button_country_list = []

        # create four button in a 1 x 4 grid
        for item in range(0, 4):
            self.option_button = Button(self.button_frame, font=("Arial", "12"),
                                         text="Option", width=30,
                                         command=partial(self.round_results, item)
                                         )
            self.option_button.grid(row=item // 2,
                                     column=item % 2,
                                     padx=5, pady=5)
            self.quiz_button_ref.append(self.option_button)

        # Button to shuffle
        self.next_button = Button(self.quiz_frame, text="Next Round",
                                  font=("Arial", "16", "bold"), fg="#FFFFFF", command=self.new_round, width=20, bg="#2E93FF")
        self.next_button.grid(row=6, pady=10)

        self.end_game_button = Button(self.quiz_frame, text="End", bg="#E23C3C", command=self.close_game, font=("Arial", "16", "bold"), fg="#FFFFFF", width=20)
        self.end_game_button.grid(row=8, padx=5, pady=5)

        self.help_stats_frame = Frame(self.quiz_frame)
        self.help_stats_frame.grid(row=7)

        # Help Button
        self.help_button = Button(self.help_stats_frame, font=("Arial", "16", "bold"),
                                   text="Help", width=9, fg="#FFFFFF",
                                   bg="#A680B8", command=self.to_hints)
        self.help_button.grid(row=0, column=0, padx=5, pady=5)

        # Stats Button
        self.stats_button = Button(self.help_stats_frame, font=("Arial", "16", "bold"),
                                   text="Stats", width=9, fg="#FFFFFF",
                                   bg="#DA67BC", command=self.to_stats)
        self.stats_button.grid(row=0, column=1, padx=5, pady=5)

        self.stats_button.config(state=DISABLED)

        # List and loop to set background colour on
        # everything except the buttons
        recolour_list = [self.quiz_frame, self.quiz_heading, self.round_label, self.round_heading, self.results_label, self.image_label, self.button_frame, self.help_stats_frame]

        for item in recolour_list:
            item.config(bg=background)

        # Once interface has been created, invoke new
        # round function for first round
        self.new_round()

    def new_round(self):
        """
        Chooses four countries' information and configures
        buttons with chosen country / capital
        """

        # Receives the country and flag chosen
        self.round_countries, self.round_country = get_round_flags()

        # Prints country name list for testing
        #print(self.round_countries)

        self.country = self.round_country[0]
        self.round_flag = self.round_country[3]
        self.round_capital = self.round_countries[1]

        # Depending on the type of quiz user chooses
        # Outputs a question and sets the column
        # array from which the option names are extracted
        # and inserted into the Button
        if self.quiztype == "Country":
            question = "Guess the Country (Hint: Flag)"
            self.count_num = 0

        else:
            question = f"What is the Capital of {self.country}"
            self.count_num = 1

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
        self.round_heading.config(text=question)
        self.round_label.config(text=f"Round {rounds_played + 1} of {rounds_wanted}")
        self.results_label.config(text=f"{'=' * 7}", bg="#FFE1C6")

        # enable country buttons (disabled at the end of the last round)
        for count, item in enumerate(self.quiz_button_ref):
            item.config(text=self.round_countries[count][self.count_num], state=NORMAL)

        self.next_button.config(state=DISABLED)

    def round_results(self, user_choice):
        """
        Retrieves which button was pushed (index 0 - 3), retrieves country name
        and checks if user was correct
        """

        # Add one to the number of rounds played and retrieve
        # the number of rounds won
        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        rounds_won = self.rounds_won.get()

        # alternate way to get button name. Good for if buttons have been scrambled!
        user_choice = self.quiz_button_ref[user_choice].cget('text')

        round_answer = self.round_country[self.count_num]

        # If chosen country name is correct, congratulates user
        if user_choice == round_answer:
            result_text = f"Amazing! {round_answer} is correct"
            result_bg = "#82B366"

            rounds_won += 1
            self.rounds_won.set(rounds_won)

        # Else displays correct answer
        else:
            result_text = f"Oops, it was {round_answer}"
            result_bg = "#F8CECC"

        self.results_label.config(text=result_text, bg=result_bg)

        # enable stats & next buttons, disable colour buttons
        self.next_button.config(state=NORMAL)
        self.stats_button.config(state=NORMAL)

        # check to see if game is over
        rounds_wanted = self.rounds_wanted.get()

        # Code for when the game ends
        if rounds_played == rounds_wanted:

            # Configure 'end game' labels / buttons
            self.round_label.config(text="Game Over")

            self.next_button.config(state=DISABLED, text="Game Over")
            self.end_game_button.config(text="Play Again", bg="#006600")

        for item in self.quiz_button_ref:
            item.config(state=DISABLED)

        # Test if rounds_won working
        #print(rounds_won)

    def close_game(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        AskRounds()
        self.play_box.destroy()

    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        DisplayHints(self)

    def to_stats(self):
        """
        Retrieves everything we need to display the quiz / round statistics
        """
        # IMPORTANT: Retrieve number of rounds
        # won as a number (rather than the 'self' container)
        rounds_won = self.rounds_won.get()
        rounds_played = self.rounds_played.get()
        stats_bundle = [rounds_won, rounds_played]

        Stats(self, stats_bundle)

class Stats:
    """
    Displays stats for Country & Capital Quiz
    """

    def __init__(self, partner, all_stats_info):

        # Setup dialogue box and background colour
        background = "#EAB3DB"

        # disable buttons to prevent program crashing
        partner.hints_button.config(state=DISABLED)
        partner.end_game_button.config(state=DISABLED)
        partner.stats_button.config(state=DISABLED)

        # Extract information from master list...
        rounds_won = all_stats_info[0]
        rounds_played = all_stats_info[1]

        self.stats_box = Toplevel()

        # Disable help button
        partner.stats_button.config(state=DISABLED)

        # If users press cross at top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box, width=350, bg=background)
        self.stats_frame.grid()

        success_rate = rounds_won / rounds_played * 100

        # Strings for Stats labels...

        rounds_string = f"Rounds Played: {rounds_played}\nRounds Won: {rounds_won}"
        success_string = f"Success Rate: {rounds_won} / {rounds_played} ({success_rate:.0f}%)"

        # custom comment text and formatting
        if success_rate == 100:
            comment_string = "Amazing! You answered all rounds correctly"
            comment_colour = "#D5E8D4"

        elif success_rate == 0:
            comment_string = "Oops - You lost every round! You might want to look at the hints!"
            comment_colour = "#F8CECC"
        else:
            comment_string = "============================"
            comment_colour = background

        heading_font = ("Arial", "16", "bold")
        normal_font = ("Arial", "14")
        comment_font = ("Arial", "13")

        # Label list (text | font | 'Sticky')
        all_stats_strings = [
            ["Statistics", heading_font, "W"],
            [rounds_string, normal_font, "W"],
            [success_string, normal_font, "W"],
            [comment_string, comment_font, "W"],
        ]

        stats_label_ref_list = []
        for count, item in enumerate(all_stats_strings):
            self.stats_label = Label(self.stats_frame, text=item[0], font=item[1],
                                     anchor="w", justify="left", bg=background,
                                     padx=30, pady=5)
            self.stats_label.grid(row=count, sticky=item[2], padx=10)
            stats_label_ref_list.append(self.stats_label)

        # Configure comment label background (for all won / all lost)
        stats_comment_label = stats_label_ref_list[3]
        stats_comment_label.config(bg=comment_colour)

        # Stats Button
        self.dismiss_button = Button(self.stats_frame, font=("Arial", "16", "bold"),
                                   text="Close", width=18, fg="#FFFFFF",
                                   bg="#DA67BC", command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=4, padx=0, pady=10)


    def close_stats(self, partner):
        # Put help button back to normal...
        partner.hints_button.config(state=NORMAL)
        partner.end_game_button.config(state=NORMAL)
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


class DisplayHints:

    def __init__(self, partner):

        # Setup dialogue box and background colour
        background = "#d7c1e2"
        self.help_box = Toplevel()

        # disable buttons to prevent program crashing
        partner.hints_button.config(state=DISABLED)
        partner.end_game_button.config(state=DISABLED)
        partner.stats_button.config(state=DISABLED)

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
                                     font=("Arial", "15", "bold"),
                                     text="Close", bg="#A680B8", width=18,
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

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country-Capital Quiz")
    Welcome()
    root.mainloop()
