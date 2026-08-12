# WAP to define a function maximum() that accepts two numbers and prints the greater number using an if-else statement.


def maximum(num1: int, num2: int):
    if num1 > num2:
        print(f'Maximum is : {num1}')
    else:
        print(f'Maximum is : {num2}')


maximum(10, 15)
maximum(105, 1)