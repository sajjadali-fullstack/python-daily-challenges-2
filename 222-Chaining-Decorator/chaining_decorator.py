# WAP to demonstrate decorator chaining by applying two decorators to a function. 
# One decorator should add $ symbols before and after the function output, 
# while another should add * symbols before and after it.



# Expected OP:- 
'''
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ******************************
# python
# ******************************
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''


# print(len('******************************'))  # 30


def draw_dollar_decorator(func):
    def draw_wrapper():

        print('$' * 30)
        func()
        print('$' * 30)

    return draw_wrapper


def draw_star_decorator(func):
    def draw_wrapper1():

        print('*' * 30)
        func()
        print('*' * 30)

    return draw_wrapper1



@draw_dollar_decorator
@draw_star_decorator
def display():
    print("python")


display()