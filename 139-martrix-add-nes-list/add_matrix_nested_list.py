# WAP to add two matrix

matrix1 = []
matrix2 = []
matrix3 = []

print("Enter elements of Matrix 1")

for i in range(2):
    row = []
    for j in range(2):
        values = int(input("Enter Values : "))
        row.append(values)

    matrix1.append(row)

# print(matrix1)  # [[10, 20], [30, 40]]

print("Enter elements of Matrix 2")

for i in range(2):
    row = []
    for j in range(2):
        elements = int(input("Enter Elements : "))
        row.append(elements)
    matrix2.append(row)

# print(matrix2)  # [[50, 60], [70, 80]]

for i in range(2):
    row = []
    for j in range(2):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)
    
print(f'Matrix 1 : {matrix1}')
print(f'Matrix 2 : {matrix2}')
print(f'Matrix 3 : {matrix3}')

# OP: -
'''
Matrix 1 : [[1, 2], [3, 4]]
Matrix 2 : [[5, 6], [7, 8]]
Matrix 3 : [[6, 8], [10, 12]]
'''