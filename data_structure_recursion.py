# Simple recursion function
def my_func(n):
    print(n)
    n -= 1
    if n == 0:
        return "I am done"
    return my_func(n)


print(my_func(3))

# Calculates factorial
def factorial_iterative(num):

    if num == 0:
        return 1

    if num <= 2:
        return num

    # starts at 2
    acc_prev = 2
    x = 0

    for current_number in range(3, num + 1):
        x = current_number * acc_prev
        acc_prev = x

    return acc_prev


print(factorial_iterative(6))
