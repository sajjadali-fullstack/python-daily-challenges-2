# WAP to read n values into list remove given value from list

list1 = []  # Empty List

n = int(input("Enter the number of values to be read : "))  # User input / length of the list

for i in range(n):
    value = int(input("Enter Elements : "))  # list elements
    list1.append(value)  # adding elements to list1

print(f'Before Deleting value : {list1}')  # printing the OG list

value = int(input("Enter the value you wanna delete : "))  # del element

if value in list1:  # CHECK : Element exist or not 
    i = list1.index(value)  # Getting Location of element
    #print(i)  # FOR CHECKING PURPOSE index show
    del list1[i]
    
    print(f'{value} is deleting from list')  #  Deleting print
    print(f'After Deleting value : {list1}')  # List1 printing after deleting element deleted
