

# WAP to demonstrate a function containing a required parameter, a default parameter,
# and variable-length positional parameters using *args.


def fun1(a, b=10, *c):  # a is required b is default, c is variable length args
    # a = Required Parameter
    # b = Default Parameter
    # c = Variable-Length Positional Parameter
    print(a, b, c)
    

fun1(100)
fun1(100, 200)
fun1(100, 200, 300, 400, 500)


# OP:-
'''
100 10 ()
100 200 ()
fun1(100, 200, 300, 400, 500)
'''