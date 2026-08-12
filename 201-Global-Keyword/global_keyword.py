# to demonstrate the use of the global keyword to modify a global variable inside a function.


# global keyword

a = 100  # Global Variable


def fun1():
    print(a)  # Accessing Global Variable


def fun2():
    global a  # Using Global Keyword
    a = 500   # Modifying Global Variable
    print(a)


def fun3():
    print(a)  # Accessing Modified Global Variable


fun1()  # Function Call
fun2()  # Function Call
fun3()  # Function Call