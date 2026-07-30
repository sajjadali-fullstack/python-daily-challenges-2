# Write a Python program to implement a simple login system using a dictionary.
# If the username and password are correct, display a welcome message;
# otherwise, display an appropriate error message.


user_dict = {'sa': 'sa123', 'sana': 'sanu786'}

user = input("Enter Username : ")
pwd = input("Enter Password  : ")

if user in user_dict:
    p = user_dict[user]
    if p == pwd:
        print(f'{user} Welcome')
    else:
        print(f'{user} Invalid Password')
else:
    print(f'{user} Invalid UserName')

