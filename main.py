# This is a math script where we are going to deal with all
# mathematical functionalities.

def add(num1, num2):
    return num1 + num2

def square(num):
    return num*num

def multiply(num1,num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("That is an invalid division, since division by 0 is not mathematically possible!")
        return "Unavailable"
    else:
        return num1 / num2

def square_root(num1):
    return num1 ** 0.5

def print_welcome_msg():
    print(f'\n\n* Hi, welcome to my program hope you have a good time\n\n')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    """Main function which is going to drive whole program"""
    print_welcome_msg()
    a = int(input("please input 1st number: "))
    b = int(input("please input 2nd number: "))
    print(f"\nResult of addition is: {add(a, b)}\n")
    print(f"\nResult of square of 1st number is: {square(a)}\n")
    print(f"\nResult of square of 2st number is: {square(b)}\n")
    print(f"\nResult of division is: {divide(a, b)}\n")
    print(f"\nResult of multiplication is: {multiply(a,b)}\n")
    print(f"\nResult of square root of 1st number is: {square_root(a)}\n")
    print(f"\nResult of square root of 2nd number is: {square_root(b)}\n")
