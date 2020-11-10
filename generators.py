# Used to cancel execution of pieces of code.
execute1, execute2, execute3 = False, False, False

def fibonacci_sequence(num):

    # Initialization. Values used only for firs item 0 of the sequence
    a, b, c = 0, 0, 0

    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
    # https://www.mathsisfun.com/numbers/fibonacci-sequence.html
    # add the first two numbers to get the third number

    # Used to count each iteration
    count = 0

    # Range starts in 0, so num+1 allows to count until the actual value passed as num as parameter
    for i in range(num + 1):

        # Edge condition. Starts the actual count.
        if i == 1:
            a, b, c = 0, 1, 0

        c = a + b

        print(f"[{count}] Previous: {a}, Current: {b}, c[{count}]: {c}\n")

        if count >= 1:
            b = a
            a = c

        count += 1

    return c


print(fibonacci_sequence(40))


if execute1:

    # Creates custom generator
    class CustomGenerator():

        current_value = 0

        # -1: Infinite sequence
        def __init__(self, last=-1):
            self.last = last

        def __iter__(self):
            return self

        def __next__(self):

            # Sequence ends at self.last
            if self.last > -1:
                self.current_value += 1
                if self.current_value > self.last:
                    raise StopIteration
                return self.current_value

            # infinite sequence
            self.current_value += 1
            return self.current_value

    # Finite sequence
    c = CustomGenerator(4)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    # print(next(c))  # raises Exception StopIteration. This is the 5th attempt and is out of the generator sequence of 4.

    # Infinite sequence. No number passed as parameter means INFINITE
    for i in CustomGenerator():
        print(i)

if execute2:

    # Creates a generator using range()
    def finite_sequence(num):
        for i in range(num):
            yield i

    # Iterates through the generator object returned by finite_sequence(10) using a for loop
    for i in finite_sequence(3):
        print(i)

    # Instead of using a for loop, call next() on the generator object(gen) directly.
    gen = finite_sequence(2)
    print(next(gen))
    print(next(gen))

    """
        Piece of code that controls exception StopIteration, sequence is two items only, and this is a 3rd attempt to get a new generator object
    """
    try:
        print(next(gen))    # This line raises the StopIteration exception
    except StopIteration:
        print("Error: passed end of sequence")


if execute3:

    # Creates a generator using a while loop that will iterate forever
    def infinite_sequence():
        num = 0
        while True:
            num += 1
            yield num

    # Iterates the generator using a for loop
    for i in infinite_sequence():
        print(i)

    # Iterates the sequence manually using next(). No need to raise an exception, next(gen) can run forever
    gen = infinite_sequence()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
