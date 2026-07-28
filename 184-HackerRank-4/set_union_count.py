
# Write a Python program to count the distinct elements from two sets using set.union().

n = int(input("Enter how many values u wanna enter : "))
s1 = set(map(int, input('Enter Numbers : ').split()))

n1 = int(input("Enter how many values u wanna enter : "))

s2 = set(map(int, input('Enter Numbers : ').split()))

s3 = s1.union(s2)

print(len(s3))