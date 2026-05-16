# WAP to generate first 10 numbers that are prime

num = 2
prime_count = 0

while True:
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c = c + 1
        if c > 2:
            break
    if c == 2:
        print(num)
        prime_count = prime_count + 1
    if prime_count == 10:
        break
    num = num + 1