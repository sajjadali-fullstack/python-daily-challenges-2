# WAP using map() and a lambda function to generate the square of every number in a list and display the results using a for loop. 


numbers = [1, 2, 3, 4, 5]

square = map(lambda n: n ** 2, numbers)

for i in square:
    print(i, end=' ')  # 1 4 9 16 25
