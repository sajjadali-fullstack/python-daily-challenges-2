# WAP Return a copy of the string with uppercase characters converted to lowercase and vice vrsa.

# input : "aBcdEfG"
# Expected OutPut : "AbCDeFg

# checking
'''
str1 = "aBcdEfG"
str2 = str1.swapcase()
print(str2)
'''

str1 = input("Enter string : ")
str2 = ''

for ch in str1:
    if ch >= 'a' and ch <='z':
        str2 = str2 + chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':
        str2 = str2 + chr(ord(ch) + 32)
    else:
        str2 = str2 + ch

print(f'Input  : {str1}')
print(f'Output : {str2}')

