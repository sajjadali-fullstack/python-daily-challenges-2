#  WAP in Python to extract the first character of each string from a given list of names
# and concatenate them into a single comma-separated string [QST]
# expected OP:- S,B,P,A,S,

name = ['Sana', 'Bushra', 'Pooja', 'Ali', 'Sajjad']

s = ''  # Empty str
# print(type(s))

for i in name:
    s = s + i[0]
    s = s + ', '

print(s)
