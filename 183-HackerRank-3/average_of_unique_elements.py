
# Write a Python program to calculate the average of all distinct (unique) elements in a list.
# Print the answer rounded to 3 decimal places.

# Example Input
'''
10
161 182 161 154 176 170 167 171 170 174
'''

# Output
# 169.375
def average(array):
    s1 = set(array)
    a = sum(s1) / len(s1)
    return round(a, 3)


n = int(input())
arr = list(map(int, input().split()))

result = average(arr)
print(result)
