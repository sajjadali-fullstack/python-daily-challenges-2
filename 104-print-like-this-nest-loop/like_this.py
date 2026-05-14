# WAP print like this 
'''
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 
'''



for row in range(5, 0, -1):
    for col in range(1, 6):
        if col >= row:
            print(col, end=" ")
        else:
            print(' ', end=' ')
    print()