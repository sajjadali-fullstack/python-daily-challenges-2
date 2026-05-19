# WAP to calculate and print the sum of all elements in a dynamically generated list using a for loop.
list1 = list(range(10, 60, 10))
print(f'Original List :  {list1}')

n = len(list1)
sums = 0
for i in range(n):
    sums += list1[i]

print(f'Sum of list element is : {sums}')
