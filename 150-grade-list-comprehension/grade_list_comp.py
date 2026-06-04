# WAP print grade wise  With Comprehension


gradeList = [['sajjad', 'B'], ['rahim', 'A'], ['Aleem', 'C'], ['faisal', 'D']]

print(gradeList)

gradeA = [i for i in gradeList if i[1] == 'A']
gradeB = [i for i in gradeList if i[1] == 'B']
gradeC = [i for i in gradeList if i[1] == 'C']
gradeD = [i for i in gradeList if i[1] == 'D']

print(f'Grade A : {gradeA}')
print(f'Grade B : {gradeB}')
print(f'Grade C : {gradeC}')
print(f'Grade D : {gradeD}')

# OP:-
'''
[['sajjad', 'B'], ['rahim', 'A'], ['Aleem', 'C'], ['faisal', 'D']]
Grade A : [['rahim', 'A']]
Grade B : [['sajjad', 'B']]
Grade C : [['Aleem', 'C']]
Grade D : [['faisal', 'D']]
'''
