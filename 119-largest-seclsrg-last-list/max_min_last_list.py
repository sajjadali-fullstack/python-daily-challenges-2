# WAP  to find the last element, largest and second largest  element from a given list. Also display the original list.

list1 = [10, 1, 4, -5, 80, 20, 10, 100, 40, 20, 10, 50]
# L -> 100, SL -> 80 Last -> 50

print(f'Original List : {list1}')

last_element = list1[-1]
print(f'Last Element : {last_element}')  # 50

list1.sort()  # Accenting order chotte se bada
max_value = list1[-1]
print(f'Maximum Value of List : {max_value}')  # 100


unique_list = list(set(list1))  # remove duplicate
unique_list.sort()

second_largest = unique_list[-2]
print(f'Second Largest Value is : {second_largest}')
