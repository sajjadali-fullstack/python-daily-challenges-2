# WAP to Reading elements from list without index
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for x in list1:
    print(x)

# OP:-
'''
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
'''
print('='*20)

for x in list1:
    for y in x:
        print(y, end=' ')
    print()

# OP:-
'''
1 2 3 
4 5 6 
7 8 9 
'''
