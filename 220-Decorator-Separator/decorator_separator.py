# WAP to create a decorator that displays a separator before and after the output of a function. Use the decorated function to display a student's name and message.


# Expected OP:-
# ==================
# Sajjad Ali
# U r so Handsome!
# ******************



def drawline_decorator(func):
    def draw_wrapper():
        print('=' * 18)
        func()

        print('*' * 18)

    return draw_wrapper


def show_name():
    print("Sajjad Ali")


def show_msg():
    print("U r so Handsome!")


@drawline_decorator
def display():
    show_name()
    show_msg()


display()