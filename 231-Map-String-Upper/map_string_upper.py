# WAP to convert all names in a list to uppercase using map() and a lambda function, without modifying the original list. 

name_list = ["sajjad", "ali", "sana", "zaya"]

up = list(map(lambda up: up.upper(), name_list))
print(up)

# OP:- 
# ['sajjad', 'sana', 'bushra']
# ['SAJJAD', 'SANA', 'BUSHRA']