# WAP to create a calculator using nested functions for addition, subtraction, multiplication, and division. 
# Use the nonlocal keyword to modify the result variable defined in the outer function.



def calculator(num1, num2, operation):
    result = None

    def add():  # Inner function
        nonlocal result
        result = num1 + num2

    def sub():  # Inner function
        nonlocal result
        result = num1 - num2

    def mul():  # Inner function
        nonlocal result
        result = num1 * num2

    def div():  # Inner function
        nonlocal result
        result = num1 / num2

    if operation == '+':
        add()
    elif operation == '-':
        sub()
    elif operation == '*':
        mul()
    elif operation == '/':
        div()
    else:
        return "Invalid Operator"

    return result


n1 = int(input("Enter Number1 : "))
n2 = int(input("Enter Number2 : "))
op = input("Enter Operator : ")
res = calculator(n1, n2, op)

print(f'Result is : {res}')
