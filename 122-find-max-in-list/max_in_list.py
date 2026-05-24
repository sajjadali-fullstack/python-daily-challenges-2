# WAP Find Max value of list
my_list = [10, 200, 30, 40, 50, 60, 70, 80, 90, 100]

max_value = my_list[0]

for i in my_list:  # i --> 10 200 30 40 50 60 70 80 90 100
    if i > max_value:  # 10 > 10 False then ... 200 > 10 True
        max_value = i
print(f'Max of this list {my_list} is : {max_value}')        

