# WAP Sorting list value s using Bubbles Sort
# Bubbles shot compares two values / elements whether1 element is > 2 element

list1 = []

n = int(input("Enter how many values u wanna insert : "))

for i in range(1, n + 1):
    value = int(input(f'Enter value {i} : '))
    list1.append(value)
print(f'\nBefore Sorting values : {list1}')

for i in range(n):
    for j in range(0, n - 1):
        if list1[j] > list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp

print(f'After Sorting values : {list1}')
