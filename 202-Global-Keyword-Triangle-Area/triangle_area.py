# WAP to accept the base and height of a triangle using one function and calculate 
# its area using another function. Use the global keyword to share the values between the functions.


base = 0.0
height = 0.0


def read():
    global base, height  # Using Global Keyword
    base = float(input("Enter Base of Triangle : "))   # Modifying Global Variable  8.0
    height = float(input("Enter Height of Triangle : "))  # Modifying Global Variable  6.0


def find_area():
    f = 0.5 * base * height  # Local variable
    print(f'Area of Triangle is : {f:.2f}')


read()
find_area()