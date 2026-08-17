# WAP  to create a generator expression that generates even numbers from 1 to 50 
# and display them using a for loop.

# Expected OP:- 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50



even = (i for i in range( 1, 51) if i % 2 == 0)

for e in even:
    print(e, end=' ')