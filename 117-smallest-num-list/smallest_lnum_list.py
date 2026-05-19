# WAP to find smallest number in a list

scores = [50, 30, 20, 10, 50, 60, -55]
a = len(scores)

for i in range(a):
    if i == 0:
        min_value = scores[i]
    elif scores[i] < min_value:
        min_value = scores[i]

print(scores)
print(f'Minimum Score : {min_value}')
