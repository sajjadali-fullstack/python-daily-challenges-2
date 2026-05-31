# WAP Remove Even elements from a list in python

list1 = [4, 9, 2, 3, 1, 11, 13, 17, 23, 8, 12, 16, 18, 20, 22]

print(f'Before Deleting values : {list1}')

i = 0
length = len(list1)

while i < length:
    if list1[i] % 2 == 0:
        del list1[i]
        length -= 1
        continue
    i += 1

print(f'After Deleting Elements {list1}')
