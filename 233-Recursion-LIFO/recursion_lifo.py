# WAP program to print 1 - 5 without using looping statements

# Expected OP:-
'''
1
2
3
4
5
'''



def display_nums(n):
    if n > 1:
        display_nums(n - 1)
    print(n)


display_nums(5)
