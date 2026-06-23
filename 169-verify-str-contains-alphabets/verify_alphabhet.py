# WAP to verify string containts only alphabets

str1 = input("Enter any strng : ").strip()

ans = True

for i in str1:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        pass
    else:
        ans = False
        break

print(ans)