# WAP Find the sum of the first 4 elements of a list.

my_list = [30, 200, 30, 40, 50, 60, 70, 80, 90, 100]

s = 0
for i in range(0,4):
    s += my_list[i]

print(f'Sum of the first 4 elements is :  {s}')  # Output: Sum of the first 4 elements is 280