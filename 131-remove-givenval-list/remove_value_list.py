# WAP to read n values into list remove given value from list

list1 = []

n = int(input("Enter the number of values to be read : "))

for i in range(n):
    value = int(input("Enter the value : "))
    list1.append(value)

print(f'Before Deleting value : {list1}')

value = int(input("Enter the value to be deleted : "))

if value in list1:
    i = list1.index(value)
    del list1[i]
    
    print(f'{value} is deleting from list')
    print(f'After Deleting value : {list1}')
