# WAP Implementing Queue Data Structure for Adding, Removing


Q = []  # empty list

while True:
    print('='*19)
    print("1. Adding")
    print("2. Removing")
    print("3. Display")
    print("4. Exit")

    option = int(input(">>> Enter option : "))

    if option == 1:
        element = input("Enter any Value : ")
        Q.append(element)

    elif option == 2:
        if len(Q) == 0:
            print("\nQueue is empty")
        else:
            value = Q[0]  # follow FIFO Method
            del Q[0]
            print(f'\n{value} deleted from Queue')

    elif option == 3:
        print(f'\n{Q}')

    elif option == 4:
        print("\nExiting Programme")
        break
    else:
        print("Invalid  Options!")
