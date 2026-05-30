# Q WAP to this input [1,1,1,2,2,2,3,4,5,6,4] to this output [1,2,3,4,5,6] QST

input_list = [1,1,1,2,2,2,3,4,5,6,4]
print(f'Original List : {input_list}')

output_list = []

for i in input_list:
    if i not in output_list:
        output_list.append(i)
print(output_list)