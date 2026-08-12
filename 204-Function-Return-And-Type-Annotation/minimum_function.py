# WAP to define a function minimum() that accepts two integers, returns the smaller number using an if-else statement,
# and displays the returned result.


def minimum(num1: int, num2: int):
    if num1 < num2:
        return num1
    else:
        return num2


res1 = minimum(10, 5)
res2 = minimum(5, 15)

print(f'Minimum is {res1}')
print(f'Minimum is {res2}')
