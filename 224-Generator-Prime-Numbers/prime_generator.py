# WAP to create a generator function that generates prime numbers within a given range using yield.
#  Use next() to retrieve prime numbers 
# one by one and then iterate over the remaining values using a for loop.




def prime_generator(start, stop):
    for num in range(start, stop + 1):
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            yield num


a = prime_generator(5, 20)  # creating prime generator iter object
v1 = next(a)
print(v1)

v2 = next(a)
print(v2)

for value in a:
    print(value)

