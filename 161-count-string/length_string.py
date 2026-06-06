# WAP to find length of string (count of characters)

count = 0

str1 = input("Enter any string : ").strip()

# print(len(str1))
for char in str1:
    count += 1
print(f'Count of {str1} is {count}')
