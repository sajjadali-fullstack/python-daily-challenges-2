# WAP to create a decorator that safely handles division by zero. 
# If the second number is zero, return 0; otherwise, perform the division using the original function.



def smart_div_decorator(func):
    def new_div_wrapper(n1, n2):
        if n2 == 0:
            return 0
        else: 
           return func(n1, n2)
    return new_div_wrapper





@smart_div_decorator
# Function Definition 
def div(n1, n2):  # Required Parameters
    res = n1 / n2
    return res


num1 = int(input("Enter 1 Number : "))
num2 = int(input("Enter 2 Number : "))

result = div(num1, num2)

print(f'{result}')