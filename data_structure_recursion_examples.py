'''
OBJECTIVE:
The example(s) in this document try to explain how recursion works behind scenes. How the magic happens.
'''

'''
This example creates 4 different functions to simulate what happens internally when a recursion function is called
Below I will break down each line of code and how it matches to recursion mechanics.

def fact4(n):

    # The two lines below replace the recursive case --> return n * fact_rec(n - 1)
    # I splitted the above recursive case to show the sequence the recursive code is executed.
    # First, the recursive function is called to get the value that will be used to multiply
    # Then, when the recursive function returns the value it will be used to perform the multiplication
    # Finally, the RESult will be returned to the calling code.

    f = fact3(3)
    res = 4 * f

    print(f"1. fact4 calling fact3. Fact3 returned {f}, and fact4 result is: {res}")
    return res

Sources:
https://www.programiz.com/python-programming/recursion
https://realpython.com/python-thinking-recursively/
https://www.python-course.eu/recursive_functions.php

    def fibi(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
https://thepythonguru.com/python-recursive-functions/
    Python stops calling recursive functions after 1000 calls by default.
    How to set the recursion limit:
        import sys
        sys.setrecursionlimit(3000)

Exercises:
http://www.cs.cmu.edu/~tcortina/activate/ct/lab8ques.pdf
'''


def fact4(n):
    f = fact3(3)
    res = 4 * f
    print(f"1. fact4 calling fact3. Fact3 returned {f}, and fact4 result is: {res}")
    return res


def fact3(n):
    f = fact2(2)
    res = 3 * f
    print(f"2. fact3 calling fact2. Fact2 returned {f}, and fact3 result is: {res}")
    return res


def fact2(n):
    f = fact1(1)
    res = 2 * f
    print(f"3. fact2 calling fact1. Fact1 returned {f}, and fact2 result is: {res}")
    return res


def fact1(n):
    print("4. Fact1")
    return 1


# print(fact4(4))


'''
The call to the recursive function as fact_rec(4) is equivalent to create the above 4 different functions
to get the factorial of the first 4 elements.
'''


def fact_rec(n):
    if n == 1:
        return 1
    else:
        f = fact_rec(n - 1)
        res = n * f
        return res  # n * fact_rec(n - 1)


# print("Factorial", fact_rec(6))


def fact_addition(n):

    if n == 0:
        return 0
    else:
        f = fact_addition(n - 1)
        res = n + f
        return res  # n + fact_addition(n - 1)


# print("Addition", fact_addition(3))


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        print(f" n {n}, n-1: {n - 1}, n-2: {n - 2}")
        n1 = recur_fibo(n - 1)
        n2 = recur_fibo(n - 2)
        return n1 + n2


print(recur_fibo(10))

# Class to call recursive function allows to keep track of how many time the recursive function is called (counter)
class FibonacciRecursive():

    # Keep track of how many times the function is called
    counter = 0

    def recur_fibo(self, n):
        if n <= 1:
            return n
        else:
            n1 = self.recur_fibo(n - 1)
            n2 = self.recur_fibo(n - 2)
            self.counter += 1
            return n1 + n2


# print("Calling class")
# f = FibonacciRecursive()
# print(f.recur_fibo(10), f.counter)

# def number_digits(n):

#     if n < 10:
#         return 1
#     else:
#         # f = int(number_digits(n - 1) / 10)
#         # print(f)
#         n = int(n / 10)
#         print(n)
#         return 1 + int(number_digits(n) / 10)


# print(number_digits(343433))













