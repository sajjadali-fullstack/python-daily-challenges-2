# WAP to use map() and a lambda function to multiply every element of a list by 2 and store the results in a new list. 


numbers = [1, 2, 3, 4, 5]

double = list(map(lambda n: n * 2, numbers))
print(double)