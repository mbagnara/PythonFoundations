# Simple recursion function
def my_func(n):
    print(n)
    n -= 1
    if n == 0:
        return "I am done"
    return my_func(n)


# print(my_func(3))

# Calculates factorial
def factorial_iterative(num):

    if num == 0:
        return 1

    if num <= 2:
        return num

    # Since the iteration starts at 3, acc_prev starts with the resultado returned by the number 2 that is 2
    acc_prev = 2

    # Range starts at 3, since numbers 0, 1 and 3 and special cases 0->1, 1->1 and 2->2
    for current_number in range(3, num + 1):
        acc_prev = acc_prev * current_number

    return acc_prev


print("Iterative", factorial_iterative(6))


def factorial_recursion(num):

    # base case
    if num == 0:
        return 1

    # base case
    if num <= 2:
        return num

    if num == 0:
        return 'Done'

    return num * factorial_recursion(num - 1)


print("Recursive", factorial_recursion(6))
