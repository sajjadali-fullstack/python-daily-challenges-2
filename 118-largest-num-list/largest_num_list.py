# WAP to find largest number in a list

scores = [1, 120, -310, 130, -50, 1500]
n = len(scores)

for i in range(n):
    if i == 0:
        max_value = scores[i]
    elif max_value < scores[i]:
        max_value = scores[i]
print(f'MaMaximum value is : {max_value}')
