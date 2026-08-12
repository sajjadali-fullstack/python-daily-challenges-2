# WAP to create a new dictionary containing only those students who have received grade B,
#  using dictionary comprehension.


grade_dict = {'Sajjad Ali': 'A', "Sana": 'A', 'Pooja': 'B', "Zaya": 'A'}
print(grade_dict)  # {'Sajjad Ali': 'A', 'Sana': 'A', 'Pooja': 'B', 'Zaya': 'A'}

print()

a = {key:value for key,value in grade_dict.items() if value == 'B'}
print(a)  # {'Pooja': 'B'}
