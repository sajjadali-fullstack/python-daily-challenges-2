# Write a Python program to perform the symmetric difference operation on two sets and print the non-common elements.

# Input
'''
Enter how many values u wanna enter : 5
Enter values : 1 2 3 4 5

Enter how many values u wanna enter : 5
Enter values : 3 4 5 6 7
'''
# Output
# {1, 2, 6, 7}

n = int(input("Enter how many values u wanna enter : "))
s1 = set(map(int, input("Enter values : ").split()))

n2 = int(input("Enter how many values u wanna enter : "))
s2 = set(map(int, input("Enter values : ").split()))

s3 = s1.symmetric_difference(s2)

s4 = list(s3)

s4.sort()

# s3 = s1 ^ s2
for i in s4:
    print(i)
