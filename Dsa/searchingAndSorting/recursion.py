# recursive function in Python to find the factorial of a number:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(factorial(num)) # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)

# second example Fibonacci Sequence:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = 6
print(fibonacci(num))  # Output: 13 (7th Fibonacci number)

# third example Sum of List Elements:
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))  # Output: 15 (1 + 2 + 3 + 4 + 5)


# forth example power calculation
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base = 2
exponent = 4
print(power(base, exponent))  # Output: 16 (2^4 = 2 * 2 * 2 * 2)
