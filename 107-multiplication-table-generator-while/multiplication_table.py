# WAP to generate the following output
'''
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30 
......

'''

num = 1  # Outer loop
while num <= 10:

    i = 1  # Inner loop
    while i <= 10:
        print(f'{num * i:4}', end=" ")  # The :4 ensures each number is right-aligned in a 4-character block
        i = i + 1
    print()
    num = num + 1
