# Error handling

def EnterAge():

    while True:
        try:
            # int() is used to determine if the input is an actual number
            your_age = int(input("What is your age?"))

            # Check if age is zero
            _ = 10 / your_age

            # Thow your own error
            #raise ValueError("Stop it right now!!")

        # Handles multiple errors
        except (ZeroDivisionError, NameError, SyntaxError) as err:
            print("Incorrect value, only numbers are allowed [{}]".format(err))
        else:
            print("Thank you!")
            break
        finally:
            print("One more attempt, do better!!")
        """
        Finally will execute ALWAYS

        Finally is a good practice for example to keep record of how many attemps
        were made before getting the right answer. Or, it could be used in a login
        routine for a user attemptimg to access the application multiple times.
        """

        """
        Exceptions raised one by one:
        ------------------------------
        except ZeroDivisionError as err:
            # "as err" is used above to capture the actual exception
            print("Zero is not allowed. Error raised: {} -->{}".format(err, "another"))
        except NameError:
            print("Enter a valid value!!")
        """

    # Out of the cycle
    print("Well done!")


EnterAge()
