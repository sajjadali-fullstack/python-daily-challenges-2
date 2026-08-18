# WAP to calculate the sum of all elements in a list using functools.reduce() 
# and a lambda function.


import functools

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

addi = functools.reduce(lambda x, y: x + y, lst1)
print(addi)  # 55

print(1+2+3+4+5+6+7+8+9+10)  # 55