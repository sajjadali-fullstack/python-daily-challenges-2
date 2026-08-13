# WAP to define a function add() that accepts any number of positional arguments using *args,
# calculates their sum, and returns the result.



def add(*values):
    total = 0

    for i in values:
        total = total + i

    return total


res1 = add(10, 20, 30)
res2 = add(10, 55)

print(f'Sum of Three is {res1}')
print(f'Sum of Two is {res2}')
