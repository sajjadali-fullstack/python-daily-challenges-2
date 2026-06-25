#  WAP PRINT HELLO FOLLOWED BY THE NAMES & THE AGE IN THE TUPLE [QST]
#  MY_TUPLE = {"CHANNEL" ,26}


my_set = {"CHANNEL", 26}
print(type(my_set))  # <class 'set'>

name = ""
age = 0


for i in my_set:
    if isinstance(i, str):
        name = i
    else:
        age = i

print(f'Hello : {name}, your age is : {age}')





