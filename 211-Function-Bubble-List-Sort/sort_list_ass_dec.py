# WAP to sort a list in ascending and descending order using a user-defined Bubble Sort function.

'''
Write a Python program that creates a function sortData() to sort the elements of a list.

1. By default, the function should sort the list in ascending order.
2. If the parameter reversed=True is passed, the function should sort the list in descending order.
3. Display the list before sorting, after ascending sorting, and after descending sorting.

'''




def sortData(a, reverse=False):
    if reverse:  # True
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if a[j] < a[j + 1]:  # a of j first element is < second ele of list
                    a[j], a[j + 1] = a[j + 1], a[j]  # Swapping
    else:
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if a[j] > a[j + 1]:  # if 1 element > second
                    a[j], a[j + 1] = a[j + 1], a[j]


# Invoke this function / Call this function
list1 = [5, 4, 8, 9, 1, 2, 3, 6, 7]
print(f'Before Sorting List               : {list1}')

sortData(list1)
print(f'After Sorting in Ascending Order  : {list1}')

sortData(list1, reverse=True)
print(f'After Sorting in descending Order : {list1}')
