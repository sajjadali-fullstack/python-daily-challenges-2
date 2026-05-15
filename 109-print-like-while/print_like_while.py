r = 5 
while r > 1:
    c = 1
    while c <= 5:
        if r == c:
            print("*", end=" ")
        else:
            print("|", end=" ")
        c = c + 1
    print()
    r = r - 1