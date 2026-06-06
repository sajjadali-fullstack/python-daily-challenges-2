# WAP to add two numbers
# input format
# # 10 20
# output
# 30

num1, num2 = map(int, input("Enter Numbers : ").split())
totals = num1 + num2
print(f'Sum of {num1} and {num2} is {totals}')
