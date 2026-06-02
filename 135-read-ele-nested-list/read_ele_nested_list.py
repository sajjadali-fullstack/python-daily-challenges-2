# WAP Reading elements from nested list using index
# Expected OP:
# 10 20 30
# 40 50 60
# 70 80 90

list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]  # 3 Rows, 9 Columns

for row in range(3):
    for col in range(3):
        print(list1[row][col], end=' ')

    print()
