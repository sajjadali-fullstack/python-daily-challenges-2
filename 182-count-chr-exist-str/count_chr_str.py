
# WAP Count of each character exist within string
# inp : abcaabbca
# Out : 5a3b2c

str1 = "abcaabbca"
str2 = ''

s1 = set(str1)  # {'a', 'c', 'b'}

for i in s1:  # abc
    c = str1.count(i)  # 432
    str2 += str(c) + i
print(str2)
