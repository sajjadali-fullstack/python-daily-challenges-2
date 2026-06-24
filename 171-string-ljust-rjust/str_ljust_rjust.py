# WAP to format and align names using ljust() and rjust() string methods.

'''
Write a Python program that stores multiple names in a list and displays them:

1. Left-aligned with a width of 10 characters.
2. Right-aligned with * as the fill character and a width of 20 characters.
3. Left-aligned with _ as the fill character and a width of 20 characters.
'''

names_list = ["Sajjad", "Ali", "Shaikh"]
for name in names_list:
    print(name.ljust(10))

print()

for i in names_list:
    print(i.rjust(20, '*'), i.ljust(20, '_'))


# Output:
"""
Sajjad
Ali
Shaikh

**************Sajjad Sajjad______________
*****************Ali Ali_________________
**************Shaikh Shaikh______________
"""