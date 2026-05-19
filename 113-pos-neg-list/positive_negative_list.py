# Display +ve and -ve values from list

list1 = [1, 2, -4, 5, -6, 6, 7, 8, 9, -10, -12, 11, -14, -13]
print(list1)

n = len(list1)

positive_count = 0
negative_count = 0

print("Reading -ve values from list1 : ")
for i in range(n):
    if list1[i] < 0:
        print(list1[i], end=" ")
        negative_count += 1
print("Reading +ve values from list1 : ")

for i in range(n):
    if list1[i] >= 0:
        print(list1[i], end=" ")
        positive_count += 1

print()
print(f'Positive Count : {positive_count}')  # 8
print(f'Negative Count : {negative_count}')  # 6


print()
print()
print()
print()

# Another way simple 

list1 = [1, 2, -4, 5, -6, 6, 7, 8, 9, -10, -12, 11, -14, -13]
print(list1)

positives = []
negatives = []

for num in list1:
    if num > 0:
        positives.append(num)
    else:
        negatives.append(num)


print("\nReding Positive(+ve) from list1 : ")
print(positives)
print()
print("Reding Negative(-ve) from list1 : ")
print(negatives)

print(f'\nPositive Count : {len(positives)}')
print(f'Negative Count : {len(negatives)}')