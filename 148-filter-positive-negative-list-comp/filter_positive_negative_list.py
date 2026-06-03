# WAP filter Positive and Negative Without Comprehension & With Comprehension


# Without Comprehension
list1 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 10, 20, 30, 4, 0 - 20, -5, -7, 60, 30]

positive_list = []
negative_list = []

for i in list1:
    if i >= 0:
        positive_list.append(i)
    else:
        negative_list.append(i)

print(f'Positive : {positive_list}')
print(f'Negative : {negative_list}')


print('=' * 35)

# With Comprehension
positive_lst = [i for i in list1 if i >= 0]
negative_lst = [value for value in list1 if value < 0]

print(f'Positive lst : {positive_lst}')
print(f'Negative lst : {negative_lst}')
