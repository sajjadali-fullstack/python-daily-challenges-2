# WAP to define a function with default parameters and demonstrate function calls using default,
# positional, and keyword arguments.


def draw_line(ch='-', length=25):  # Default Parameters
    for i in range(length):
        print(ch, end='')
    print()


draw_line()  # Default Argument
draw_line('$')  # Positional Argument
draw_line(ch='|', length=3)  # keyword Argument
