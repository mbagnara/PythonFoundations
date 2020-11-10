def DecoratorFunction(fn):
    import time

    # Used to keep count of how many times the decorator is called
    count = 0

    def wrapper():

        # Counts the number of calls. Keeps the value between calls
        nonlocal count
        count += 1

        # Start message
        print("Internal wrapper function: Initiating...")

        # Gets when the function bound to the decorator starts executing
        time.sleep(1)
        t1 = time.time()

        # Invokes the function bound to the decorator
        fn()

        # Calculates when the function finishes executing
        t2 = time.time()

        # Prints final messages
        print("Internal wrapper function: Initiating...")
        print(f"function took {t2 - t1} seconds to run. Called {count} time(s)\n")  # new style
        # print("function took {} seconds to run".format(t2 - t1))
    return wrapper


@DecoratorFunction
def PrintMessage():
    print("Holasss")


# Calling the function that executes the decorator 3 times.
my_print_function = PrintMessage
for i in range(3):
    my_print_function()
