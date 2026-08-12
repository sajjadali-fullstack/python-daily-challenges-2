# WAP to define a function simple_interest() that accepts
# amount, time, and rate as parameters, calculates simple interest, returns the result,
# and displays it up to two decimal places.

def simple_interest(amt, time, rate):
    simple_int = (amt * time * rate) / 100
    return simple_int


result = simple_interest(10000, 12, 2.5)
print(f'Simple Interest\n{result:.2f}')
