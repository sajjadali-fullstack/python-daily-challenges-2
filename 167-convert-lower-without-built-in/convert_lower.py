# WAP to convert to string into lowercase

str1 = "ALI"
str2 = ''

for ch in str1:
    if ch >= 'A' and ch <= 'Z':
        str2 = str2 + chr(ord(ch) + 32)

print(f'Original String : {str1}')
print(f'Conver into lower : {str2}')
