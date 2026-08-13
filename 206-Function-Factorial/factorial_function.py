# WAP to define a function factorial() that accepts an integer, calculates its factorial using a loop,
# returns the result, and displays the factorial of the given number.

def factorial(num:int) -> int:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


number = int(input("Enter any number : "))
res = factorial(number)
print(f'Factorial of {number} is {res}')