# Write a Python program to input two sets and determine whether the first set is a subset of the second set.
# Print True or False.


# Input Format
'''
Enter number of test cases: 1
Enter number of elements in Set A: 5
Enter elements of Set A: 1 2 3 4 5
Enter number of elements in Set B: 7
Enter elements of Set B: 1 2 3 4 5 6 7
'''
# Output 
# True




T = int(input("Enter number of test cases: "))

for i in range(T):
    m = int(input("Enter number of elements in Set A: "))
    A = set(map(int, input("Enter elements of Set A: ").split()))

    n = int(input("Enter number of elements in Set B: "))
    B = set(map(int, input("Enter elements of Set B: ").split()))

    print(A.issubset(B))