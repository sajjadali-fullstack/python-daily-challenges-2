# WAP to count and display all the even and odd numbers from a given list.

list1 = [10, 20, 30, 3, 2, 1, 5, 33, 99, 32]
print(f'Original List :  {list1}')

even_count = 0
odd_count = 0

even_numbers = []
odd_numbers = []

for i in list1:
    if i % 2 == 0:
        even_count += 1
        even_numbers.append(i)
    else:
        odd_count += 1
        odd_numbers.append(i)
print(f'\nEven Numbers : {even_numbers}')
print(f'Even Count : {even_count}')
print("="*35)
print(f'Odd Numbers : {odd_numbers}')
print(f'Odd Count : {odd_count}')
