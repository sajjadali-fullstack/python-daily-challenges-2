# WAP to create a login system using an infinite loop that repeatedly asks the user for a username and password. 
# If the credentials match, display a welcome message and exit the loop;
# otherwise, show an error message and ask again

while True:
    
    user = input("UserName : ") 
    pwd = input("Password  : ")
    if user == 'sa' and pwd == 'sa123':
        print(f'Welcome {user}')
        break
    else:
        print("Invalid Username or Password")