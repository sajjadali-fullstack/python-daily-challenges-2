# WAP using generator expressions to generate even and odd numbers from a range,
#  filter even and odd values from a list, 
# and generate list elements in reverse order.




# Generator Expression

ev = (i for i in range(1, 61) if i % 2 == 0)  # Even Data
print(ev)
for value in ev:
    print(value, end=' ')
print()

print()

od = (i for i in range(1, 61) if i % 2 != 0)  # Odd Data
for val in od:
    print(val, end=' ')

print()


print()
lst1 = [1, 2, 3, 6, 8, 9, 24, 58, 84, 12, 11, 16, 16, 7, 88, 49]

e = (values for values in lst1 if values % 2 == 0)
o = (values for values in lst1 if values % 2 != 0)

print('Even Data...')
for value in e:
    print(value, end=' ')

print()
print()

print("Odd Data...")
for value in o:
    print(value, end=' ')
print()


print()
lst = [10, 20, 30, 40, 50]

a = (value for value in lst[::-1])
for value in a:
    print(value, end=' ')
