# WAP to create a simple sign-in system using a dictionary. 
# Define a function that accepts a username and password and returns True if both credentials are correct; otherwise, return False.

users = {'sa': 'sa123', 'as': 'as123', 'ps': 'sa123'}


def signin(u, p):
    if u in users and users[u] == p:  # if "sa" in users and users["sa"] == "sa123":
        return True
    else:
        return False


user = input("UserName : ")
pwd = input("Password : ")

if signin(user, pwd):
    print(f'{user.title()} Welcome')
else:
    print('Incorrect Username / password')
