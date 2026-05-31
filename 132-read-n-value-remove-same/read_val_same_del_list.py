# WAP to read n values into list, Remove given values from list

list1 = []
n = int(input("Enter how many values : "))
for i in range(n):
    values = int(input("Enter a value : "))
    list1.append(values)

print(f'Before Deleting Values : {list1}')
value = int(input("Enter value to delete : "))

found = False
while True:
    if value in list1:
        i = list1.index(value)
        del list1[i]
        found = True
    else:
        break
if found == True:
    print(f'After Deleting Element : {list1}')
else:
    print(f'{value} not exist in list')
