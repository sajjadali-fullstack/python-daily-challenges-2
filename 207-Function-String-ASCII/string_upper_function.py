# WAP a function to convert string to uppercase

# WAP to define a function upper() that converts all lowercase characters of a string
# into uppercase using ord() and chr()
# without using the built-in upper() method.


# a --> A  -32, A --> a + 32

def upper(s: str) -> str:
    upper_string = ''

    for ch in s:
        if ch >= 'a' and ch <= 'z':
            upper_string = upper_string + chr(ord(ch) - 32)
        else:
            upper_string = upper_string + ch
    return upper_string

str1 = input("Enter any string : ")
str2 = upper(str1)

print(str1)
print(str2)
