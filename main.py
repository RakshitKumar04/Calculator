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
    
def sqroot(num):
    return math.sqrt(num)
      
def cube(number):
    return number*number*number
  
def substract(num1, num2):
    return num1 - num2

def square_root(num1):
    if num1 < 0:
        print("Square root of negative number results to complex number, which is not supported here.")
        return "Unavailable"
    else:
        return num1 ** 0.5

def print_welcome_msg():
    print(f'\n\n* Hi, welcome to my program hope you have a good time\n\n')  # Press Ctrl+F8 to toggle the breakpoint.

def fact(num):
    fct = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fct = fct * i
        return fct;


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
    print(f"\nResult of cube of 1st number is: {cube(a)}\n")
    print(f"\nResult of cube of 2nd number is: {cube (b)}\n")
    print(f"\nResult of 1st minus 2nd number is: {substract(a,b)}\n")
    print(f"\nResult of 2nd minus 1st number is: {substract(b,a)}\n")
    print(f"\nResult of factorial of 1st number is: {fact(a)}\n")
    print(f"\nResult of factorial of 2nd number is: {fact(b)}\n")
    print(f"\nResult of 2nd minus 1st number is: {substract(b,a)}    
    print(f"\nResult of square root of 1st number is: {sqroot(a)}\n")
    print(f"\nResult of square root of 2nd number is: {sqroot(b)}\n")
