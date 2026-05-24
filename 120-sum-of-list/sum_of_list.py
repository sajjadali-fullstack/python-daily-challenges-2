# Add The Value of the List using for loop
# WAP  to calculate the sum of a list using a for loop

my_list = list(range(10, 110, 10))
#print(my_list)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sums = 0

for x in my_list:
    sums = sums + x
print(f'Sum of {my_list} is :  {sums}')