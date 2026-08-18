# WAP to add corresponding elements of two lists using map() 
# and a lambda function, and store the results in a new list.


lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 20, 30, 40, 50]

adding = list(map(lambda v1, v2: v1 + v2, lst1, lst2))

print(adding)  # [11, 22, 33, 44, 55]
