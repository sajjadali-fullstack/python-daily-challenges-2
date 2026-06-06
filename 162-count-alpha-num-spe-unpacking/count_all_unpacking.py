# WAP to count alphabets, digits and special character exists within string using unpacking

count = 0
str2 = input("Enter any string : ")
alphabet_count, digit_count, special_count = 0, 0, 0  # unpacking

for i in str2:
    if 'a' <= i <= 'z' or 'A' <= i <= 'z':
        alphabet_count += 1
    elif i >= '0' and i <= '9':
        digit_count += 1
    else:
        special_count += 1

print(f'Alphabet Count : {alphabet_count}')
print(f'Digits count   : {digit_count}')
print(f'Special Count  : {special_count}')
