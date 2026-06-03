
# Create a list with n values Without Comprehension & with Comprehension

# 1. Without Comprehension
print("Without Comprehension")
print('-'*23)

n = int(input("Enter value of n : "))
lst = []

for i in range(1, n + 1):
    values = int(input(f'Enter Element {i} : '))
    lst.append(values)

print(lst)

print('='*15)

# 2. With Comprehension
print("With Comprehension")
print('-'*20)

n = int(input("Enter value of n : "))
lst1 = [int(input(f'Enter {i} value : ')) for i in range(1, n + 1)]
print(lst1)
