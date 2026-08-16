#  WAP to create a decorator that adds a heading and separator around the output of a student details function.


# Expected OP:- 
'''
Yo!
***************
Python
Name : Sajjad
===============

'''
# print(len('***************'))  # 15




def drawline(fun1):  # decorator
    def draw():  # wrapper

        print('Yo!')
        print('*' * 15)
        fun1()
        print('=' * 15)

    return draw



def stu_info():
    print('Python')
    print('Name : Sajjad')


@drawline
def dis_stu():
    stu_info()

dis_stu()