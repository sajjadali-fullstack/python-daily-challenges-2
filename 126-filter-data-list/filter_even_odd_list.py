# WAP Filter Data: Even & Odd
num_list = [2, 8, 1, 2, 9, 5, 11, 15, 17, 18, 21, 89, 34, 56, 87, 23, 32, 37, 87, 56, 45, 34, 23, 12]

even_list = []  # Empty list
odd_list = []  # Empty list

for num in num_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(f'Number List : {num_list}')
print("Even numbers List : ", even_list)
print("Odd numbers List : ", odd_list)
