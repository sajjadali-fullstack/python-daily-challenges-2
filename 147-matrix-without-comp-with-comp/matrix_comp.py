# WAP to read 2X2 matrix

matrix = []  # empty list

# Without Comprehension
for i in range(2):
    row = []  # [][]

    for j in range(2):
        value = int(input("Enter value : "))
        row.append(value)
    matrix.append(row)

print(matrix)

print('='*20)

# With Comprehension
matrix = [[int(input("Enter Element : ")) for j in range(2)] for i in range(2)]
print(matrix)
