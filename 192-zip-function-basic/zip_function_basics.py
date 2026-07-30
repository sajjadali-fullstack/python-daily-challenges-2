# WAP to combine two lists into pairs using the zip() function and print each pair.

lst1 = [1, 2, 3]
lst2 = [10, 20, 30]
# print(list(zip(lst1, lst2)))
print(*zip(lst1, lst2))  # (1, 10) (2, 20) (3, 30)
