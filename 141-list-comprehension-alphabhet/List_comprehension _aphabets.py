# WAP List comprehension with Alphabets from A-Z

print(ord('A'))  # 65
print(ord('Z'))  # 90

lst = [chr(i) for i in range(65, 91)]
print(lst)  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']