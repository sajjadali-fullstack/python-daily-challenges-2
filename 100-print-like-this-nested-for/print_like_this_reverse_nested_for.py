# Q. WAP to take number from user and print it reversed [QST]
'''
EG:

Enter some Number : 5
5  5  5  5  5  
4  4  4  4  4  
3  3  3  3  3  
2  2  2  2  2  
1  1  1  1  1  

'''

num = int(input("Enter any number : "))

for i in range(num, 0, -1):
    for j in range(1, num + 1):
        print(i, end="  ")
    print()