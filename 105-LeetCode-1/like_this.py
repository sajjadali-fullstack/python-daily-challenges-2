# WAP to print like this 
'''
7 4 1
8 5 2
9 6 3
'''

for i in range(7, 10):
    for j in range(3):
        print(i - j * 3, end=" ")
    print()
