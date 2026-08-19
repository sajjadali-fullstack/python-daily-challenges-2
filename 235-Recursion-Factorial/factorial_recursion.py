# WAP to find factorial of input numbers


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter any numbers : "))
result = factorial(num)
print(f'factorial of {num} is {result}')