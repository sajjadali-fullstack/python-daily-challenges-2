# Find Medium

list1 = [10, 20, 30, 40]
# list1 = [10, 20, 30, 40, 50]

n = len(list1)

if n % 2 != 0:
    mid_value = n // 2
    print(f'Median of {list1} is : {list1[mid_value]}')
else:
    mid_value = n // 2
    print(f'Median of {list1} is {(list1[mid_value] + list1[mid_value - 1]) // 2}')
