# WAP to create a new dictionary containing only those students who have received grade B,
#  using dictionary comprehension.


grade_dict = {'Sajjad Ali': 'A', "Sana": 'A', 'Pooja': 'B', "Zaya": 'A'}
print(grade_dict)  # {'Sajjad Ali': 'A', 'Sana': 'A', 'Pooja': 'B', 'Zaya': 'A'}

print()

gradeAdict = {key:value for key,value in grade_dict.items() if value == 'A'}
print(gradeAdict)  #  {'Sajjad Ali': 'A', 'Sana': 'A', 'Zaya': 'A'}

print()

gradeBdict = {name:grade for name, grade in grade_dict.items() if grade == 'B'}
print(gradeBdict)  # {'Pooja': 'B'}