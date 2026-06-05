# Q.7 CREATE A NEW LIST THAT CONTAINS THE LAST ELEMENTS IN THE NESTED LISTS [QST]

# Expected OP: ['chocolate', 'potatoes', 'protein bar']

grocery_list = [["chips", "jelly", "chocolate"], ["sweet potatoes", "potatoes"], ['peanuts', "protein bar"]]

new_lst = [grocery_list[0][-1], grocery_list[1][-1], grocery_list[2][-1]]

print(f'Original List : {grocery_list}')
print(f'New List : {new_lst}')  # New List : ['chocolate', 'potatoes', 'protein bar']

print('='*120)
print("Another WAY")

new_lst1 = []
for sub_list in grocery_list:
    new_lst1.append(sub_list[-1])

print(f'Original List : {grocery_list}')
print(f'New List : {new_lst1}')
