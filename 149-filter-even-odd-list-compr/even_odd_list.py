# WAP filter Even and Odd With Comprehension

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst1 = [i for i in list1 if i % 2 == 0]
lst2 = [i for i in list1 if i != 2]

print(f'Even List : {lst1}')
print(f'Odd List  : {lst2}')
