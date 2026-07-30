# Write a Python program to create a dictionary from a list where the keys are the index positions and the values are the corresponding list elements.

lst = [10, 20, 30, 40, 50]

e1 = enumerate(lst)
print(type(e1))  # <class 'enumerate'>

d1 = dict(e1)
print(type(d1))  # <class 'dict'>

print(d1)  # {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}