# WAP to demonstrate the difference between global and local variables when the same variable name is used inside a function.


x = 100  # Global Variables


def fun1():
    y = 200  # Local variable
    print(f'Global variable x={x}')
    print(f'Local variable y={y}')


def fun2():
    z = 300  # Local variable
    x = 500  # Local variable
    print(f'Local variable z={z}')
    print(f'Local variable x={x}')


fun1()  # Function Call / Executable Statement
fun2()  # Function Call / Executable Statement

