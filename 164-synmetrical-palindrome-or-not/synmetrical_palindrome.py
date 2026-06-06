# WAP check entered string is symmetrical or not ?
# EG: ama ama
# OP :- both are v both are palindrome

str4 = input("Enter any string : ")
# str4 = "ama ama"

length = len(str4)  # 7
m = length // 2  # 0

if length % 2 == 0:
    s1 = str4[:m]  #
    s2 = str4[m:]  # ama ama
else:
    s1 = str4[:m]
    s2 = str4[m+1:]

if s1 == s2:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if str4 == str4[::-1]:
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")

# Explain:-
'''
How it runs with "ama ama":
    length = 7 (odd)
    m = 3 
    s1 = str4[:3] --> "ama"
    s2 = str4[4:] --> "ama" (skipping the space at index 3)
    s1 == s2 is True --> Symmetrical!
    str4 == str4[::-1] is True --> Palindrome!
'''
