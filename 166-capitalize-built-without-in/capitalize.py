# WAP to capitalize string
# from builtins function and without

str1 = input("Enter any string : ")
str2 = str1.capitalize()

print(f'Original string : {str1}')
print(f'Capitalize string : {str2}')

print('='*32)

# Without In Build

characters = input("Enter any string : ")
changes = ''  # empty str

for i in range(len(characters)):  # 0 1 2 3 4 5
    if i == 0:
        if characters[i] >= 'a' and characters[i] <= 'z':
            changes = changes + chr(ord(characters[i]) - 32)
        else:
            changes = changes +characters[i]
    elif characters[i] >= 'A' and characters[i] <='Z':
        c2 = changes + chr(ord(characters[i]) + 32)
    else:
        changes = changes + characters[i]

print(f'Original String : {characters}')
print(f'Capitalize string : {changes}')
