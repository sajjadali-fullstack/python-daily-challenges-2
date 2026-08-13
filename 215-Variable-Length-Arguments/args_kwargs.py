# WAP to demonstrate variable-length arguments using *args and **kwargs. 
# Use *args to accept multiple positional values and **kwargs to accept 
# multiple keyword arguments, then display the received values.



def display_stud_info(**kwargs):  # dict
    for name, course in kwargs.items():
        print(f'{name} --> {course}')


def display_tuple(*vargs):  # tuple
    for value in vargs:
        print(value)


stud_dict = {'sa': "Python", "sana": "Builder"}
display_stud_info(**stud_dict)

t1 = (10, 20, 30)
display_tuple(*t1)
