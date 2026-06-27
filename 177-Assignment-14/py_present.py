# WAP to check whether a specific element exists in a tuple using the in and not in operators. [QST]

'''
Write a Python program that creates a tuple of subject names and checks whether the string "python" is present in the tuple.
If it exists, print "True"; otherwise, print "False".
'''

my_tuple = ('math', 'science', "python", "english")


if "python" not in my_tuple:
    print("False")
else:
    print("True")
