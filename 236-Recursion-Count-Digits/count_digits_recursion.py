# WAP to count digits or find lengths of numbers

result = -1

def count_digits(n):
    global result

    if n != 0:
        count_digits(n // 10)
    result += 1


digits = int(input("Enter any numbers : "))
count_digits(digits)

print(f' Digits is {digits} & Count is : {result}')