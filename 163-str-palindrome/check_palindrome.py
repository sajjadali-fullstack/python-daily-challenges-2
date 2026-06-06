# WAP to check if a string is palindrome or not
# madam --> madam ,

str3 = input("Enter any string : ")
check = str3[::-1]
if str3 == check:
    print(f'{str3} is Palindrome')
else:
    print(f'{str3} is not Palindrome')

