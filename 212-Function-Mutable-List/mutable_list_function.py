# WAP to demonstrate how a mutable list can be modified inside a function by passing the list as an argument.



def fun1(a):  # required type
    a[0] = 99
    a.append(100)


def fun2():
    lst1 = [10, 20, 30]
    print(f'Before Calling Function : {lst1}')
    fun1(lst1)  # object reference is passed to the function.
    print(f'After Calling Function : {lst1}')


fun2()  # calling


# Before Calling Function : [10, 20, 30]
# After Calling Function : [99, 20, 30, 100]