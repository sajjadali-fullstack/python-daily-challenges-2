# Write a Python program to create a dictionary from a list where the keys start from a given index using enumerate().


sales_list = [5000, 6000, 7000, 8000, 9000]
print(type(sales_list))  # <class 'list'>
print(sales_list)  # [5000, 6000, 7000, 8000, 9000]

e2 = enumerate(sales_list, 2000)
print(type(e2))  # <class 'enumerate'>

d2 = dict(e2)
print(type(d2))  # <class 'dict'>
print(d2)  # {2000: 5000, 2001: 6000, 2002: 7000, 2003: 8000, 2004: 9000}