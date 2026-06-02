# WAP Creating nested list by input values at run time [OR] create 3x3 matrix

matrix = []  # empty matrix

for r in range(3):
    row = []  # [] [] []
    for c in range(3):
        elements = int(input("Enter value : "))
        row.append(elements)
    matrix.append(row)
print(matrix)  # [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
