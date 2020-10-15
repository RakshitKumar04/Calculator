# This is a math script where we are going to deal with all
# mathematical functionalities.
import math
def add(num1, num2):
    return num1 + num2

def print_welcome_msg():
    print(f'\n\n* Hi, welcome to my program hope you have a good time\n\n')  # Press Ctrl+F8 to toggle the breakpoint.
    
def sqrt(num1):
    if num1 < 0:
        return (f'{math.sqrt(abs(num1))}i')
    else:
        return math.sqrt(num1)
    
if __name__ == '__main__':
    """Main function which is going to drive whole program"""
    print_welcome_msg()
    a = int(input("please input 1st number: "))
    b = int(input("please input 2nd number: "))
    print(f"\nResult of addition is: {add(a, b)}\n")
    print(f"\nSquare root of number is: {sqrt(a)}\n")
