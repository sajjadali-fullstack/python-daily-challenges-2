# WAP program to print 5 to 1 without using looping statements


def rev_nums(n):
    if n < 5:
        rev_nums(n + 1)
    print(n)


rev_nums(1)
