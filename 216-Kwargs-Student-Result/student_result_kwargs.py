# WAP using **kwargs to accept student details such as roll number, name, and subject marks. 
# Display the student information and determine whether 
# the student has passed or failed based on the subject marks.



def result(**kwargs):
    print(f'Roll no :  {kwargs["rollno"]}')
    print(f'Name :     {kwargs["name"]}')
    print(f'Subject1 : {kwargs["sub1"]}')
    print(f'Subject2 : {kwargs["sub2"]}')

    if kwargs['sub1'] < 40 or kwargs['sub2'] < 40:
        print("\nResult Fail")
        print('-' * 11)
    else:
        print("\nResult Pass")
        print('-' * 11)


result(rollno=128, name='Sajjad Ali', sub1=68, sub2=79)
print('='*15)
result(name='Faisal', rollno=16, sub1=15, sub2=12)



# OP:- 

'''

Roll no :  128
Name :     Sajjad Ali
Subject1 : 68
Subject2 : 79

Result Pass
-----------

===============
Roll no :  16
Name :     Faisal
Subject1 : 15
Subject2 : 12

Result Fail
-----------

'''