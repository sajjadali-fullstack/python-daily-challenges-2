# WAP List comprehension Create copy of list by converting all names in uppercase

names_list = ["sajjad ali", "sana", "pooja"]

ls1 = [i for i in names_list]
print(f'Original List    : {ls1}')

ls2 = [i.upper() for i in names_list]
print(f'After Converting : {ls2}')
