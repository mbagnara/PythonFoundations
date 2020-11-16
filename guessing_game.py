'''
This is a guessing game that can run from the command in two modes:
1. Without user interaction
    example:
        $ python guessing_game 10 3

2. With user interaction
    This option is enabled in the code itsel setting user_input to True
'''

import random
import sys


def maximum_guesses():
    '''
        1: Validates a valid number is entered (ValueError)
        2: Validates a number is passed. If no value is entered, exception is raised (IndexError)
    '''

    # -1 means validation did not pass
    max_guesses = -1

    try:
        max_guesses = int(sys.argv[1])
    except ValueError:
        print("Param-Maximum Guesses: You did not enter a valid number. Please try again")
    except IndexError:
        print("You did not enter a number. Please try again")

    return max_guesses


def maximum_rounds():
    max_rounds = 1

    try:
        max_rounds = int(sys.argv[2])
    except ValueError:
        max_rounds = -1
        print("Param-Maximum Rounds: You did not enter a valid number. Please try again")
    except IndexError:
        max_rounds = 1  # No value was entered, so the default (1) is assumed

    return max_rounds


def guessing_game():
    print("Starting THE Guessing Game...")

    user_input = False  # Enables user interaction
    max_guesses = 10    # Default value
    max_rounds = 1      # Default value
    line = "-" * 70

    '''
        Parameteres:
        sys.argv[1]: Number of guesses
        sys.argv[2]: Round of guesses
    '''

    # This option allows user to enter information in the console
    if user_input:

        valid_number = False

        while valid_number is False:

            try:
                max_guesses = int(input("Enter the number of guesses you want: "))
                valid_number = True
            except ValueError:
                print("You did not enter a number. Please try again")

    # This option allows information to enter directly in the command line when calling the program
    else:

        max_guesses = maximum_guesses()
        if max_guesses == -1:
            return

        # Default is 1
        max_rounds = maximum_rounds()
        if max_rounds == -1:
            return

    summary = []

    for i in range(1, max_rounds + 1):

        print(line)
        print(f"STARTING THE GUESSING GAME. Round {i} of {max_rounds}")

        guesses = 1

        while guesses <= max_guesses:

            # User entered random value
            guessed_number = random.randint(1, max_guesses)

            # Machine calculated randon number
            machine_number = random.randint(1, max_guesses)

            print(f"\tAttempt: [{guesses}] User number: {guessed_number}, machine number: {machine_number}")
            guesses += 1

            if guessed_number == machine_number:
                summary.append(f"Round {i} of {max_rounds}. Attempt: [{guesses}] Gussed number: {guessed_number}")
                print("Good job! Guessed the number")
                break

        # Blank line
        print(line)
        print("")

    # Display summary of guesses
    print("Guessing Game Has Ended!!")

    '''
        Don’t check for empty containers or sequences (like [] or '') by comparing the length to zero (if len(somelist) == 0). Use if not somelist and assume that empty values will implicitly evaluate to False.

        (if list) is True means not empty. Empty lists evaluate to false
    '''
    if summary:  # non-empty
        print("")
        print(line)
        print("SUMMARY")
        print(line)
        for i in summary:
            print(i)
        print(line)
    else:
        print("")
        print("No matching guesses were found. Sorry, try again!")


guessing_game()
