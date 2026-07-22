# Write a Python program to count the number of occurrences of each value in a list.

''''
Input:
list1 = [10, 20, 30, 10, 10, 20, 30, 30, 50]

Output:
10 --> 3
20 --> 2
30 --> 3
50 --> 1
'''

list1 = [10, 20, 30, 10, 10, 20, 30, 30, 50]

set1 = set(list1)

for i in set1:
    c = list1.count(i)
    print(f'{i} --> {c}')