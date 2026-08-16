# Perfect Numbr using Function

start_num = int(input("Enter starting value : "))
end_num = int(input("Enter ending value : "))

while start_num <= end_num:
    i = 1
    s = 0

    while i < start_num:
        if start_num % i == 0:
            s = s + i
        i = i + 1
    if s == start_num:
        print(start_num)
    start_num = start_num + 1