# WAP to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output: [24, 35, 9, 56, 12]

list1 = [12, 35, 9, 56, 24]

print(f'Original List :  {list1}')

# 1 approach

x = list1[0]  # 12
list1[0] = list1[-1]  # replace
list1[-1] = x
print(f'After Swapping : {list1}')

print('=' * 37)
# 2 approach

list1[0], list1[-1] = list1[-1], list1[0]
print(f'After Swapping : {list1}')
