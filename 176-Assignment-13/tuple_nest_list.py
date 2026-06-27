#WAP to access elements from a tuple containing a nested list.

'''
Write a Python program that creates a tuple containing integers and a nested list. Display:

1. The element 10 from the nested list.
2. The first two elements of the nested list using slicing.
'''


my_tuple = (40, 3, 2, [10, 4])

print(my_tuple[3][0])
print(my_tuple[3][0:2])