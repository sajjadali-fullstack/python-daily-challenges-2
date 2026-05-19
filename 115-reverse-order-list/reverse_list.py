# WAP to print all the elements of a given list in reverse order using a for loop and negative indexing.

list1 = [10, 20, 30, 3, 2, 1, 5, 33, 99, 32]
n = len(list1)
print(f'Original List :  {list1}')

for i in range(-1, -(n + 1), -1):
    print(list1[i], end=' ')

# Another ways
print()

print((list1[::-1]))
