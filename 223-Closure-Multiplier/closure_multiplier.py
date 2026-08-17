# WAP to demonstrate a closure where an inner function remembers and uses a variable from its enclosing function 
# even after the outer function has finished execution.


def multiplier(x):
    def multiple(y):
        print(x * y)

    return multiple

double = multiplier(5)  # double ke andar inner function hai aur usko x = 5 yaad hai.
double(2)  # 10
double(5)  # 25