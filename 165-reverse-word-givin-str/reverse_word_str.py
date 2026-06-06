# WAP Reversed Word in a given String in Python
# Input :- "greek quiz practice code"
# Output :- code practice quiz geeks

str8 = "greek quiz practice code"
print(f'Input  : {str8}')

list5 = str8.split()  # ['greek', 'quiz', 'practice', 'code']
list5 = list5[::-1]  # ['code', 'practice', 'quiz', 'greek']

str9 = ' '.join(list5)
print(f'Output : {str9}')  # code practice quiz greek
