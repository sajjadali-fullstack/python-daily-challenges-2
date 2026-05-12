# WAP to take an integer input from the user and display a character pattern of size. 
# The first row should consist of 'A's, the second row of 'B's, and so on. [QST]

alphabet = int(input("Enter any number to see an Alphabet : "))

for i in range(alphabet):
    for j in range(alphabet):
        print(chr(i + 65), end="  ")
    print()