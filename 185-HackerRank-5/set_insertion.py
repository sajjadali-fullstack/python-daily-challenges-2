# Write a Python program to perform the intersection operation on two sets and print the common elements.

# Input
'''
Enter how many values u wanna enter : 5
Enter values : 1 2 3 4 5

Enter how many values u wanna enter : 5
Enter values : 3 4 5 6 7
'''
# Output
# {3, 4, 5}

n = int(input("Enter how many values u wanna enter : "))
s1 = set(map(int, input("Enter values : ").split()))

n2 = int(input("Enter how many values u wanna enter : "))
s2 = set(map(int, input("Enter values : ").split()))

check = s1.intersection(s2)
print(check)
