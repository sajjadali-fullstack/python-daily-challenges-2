# Given a list in python amd provided the positions of the elements,WAP to swap the two elements in the list
# Examples :
# Input : [23, 65, 19,90]  # user change : pos1 : 1, pos2 : 3
# Output : [19, 65, 23, 90]

# Input : [1, 2, 3, 4, 5]  # user change : pos1 : 2, pos2 : 5
# Output : [1, 5, 3, 4, 2]


list1 = []  # empty list
n = int(input("How many element u want to enter : "))  # eg.5

for i in range(1, n + 1):
    value = int(input(f'Enter value {i} : '))
    list1.append(value)

print(f'list Before Swapping : {list1}')

position1 = int(input("Enter position 1 : "))
position2 = int(input("Enter position 2 : "))

temp = list1[position1 - 1]
list1[position1 - 1] = list1[position2 - 1]
list1[position2 - 1] = temp
# print(temp)
print(f'List after swapping : {list1}')
