# This is a math script where we are going to deal with all
# mathematical functionalities.

def pow(num1,num2):
    power = 1

    for i in range(1, num2 + 1):
        power = power * num1
    return power

def print_welcome_msg():
    print(f'\n\n* Hi!, Welcome to my program hope you have a good time.\n\n')

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error! Invalid division. Division by 0 is not mathematically possible.")
        return "Error! Division by Zero"
    else:
        return num1 / num2
    
def square(num):
    return num*num

def cube(num):
    return num*num*num
  
def square_root(num):
    if num < 0:
        print("Square root of negative number results to complex number, which is not supported here.")
        return "Error! Square root of negative number"
    else:
        return num ** 0.5
 
def cube_root(num):
    return num**(1/3)

def factorial(num):
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
    
def average(num1, num2):
    avg = float((a+b)/2)
    return avg

if __name__ == '__main__':
    """Main function which is going to drive whole program"""
    
    print_welcome_msg()
    
    a = int(input("please input 1st number: "))
    b = int(input("please input 2nd number: "))
    
    print(f"\nResult of addition is: {add(a, b)}\n")

    print(f"\nResult of 1st substract 2nd number is: {substract(a,b)}")
    print(f"\nResult of 2nd substract 1st number is: {substract(b,a)}\n")

    print(f"\nResult of multiplication is: {multiply(a,b)}\n")
    
    print(f"\nResult of division is: {divide(a, b)}\n")

    print(f"\nResult of square of 1st number is: {square(a)}")
    print(f"\nResult of square of 2st number is: {square(b)}\n")
    
    print(f"\nResult of cube of 1st number is: {cube(a)}")
    print(f"\nResult of cube of 2nd number is: {cube(b)}\n")
    
    print(f"\nResult of average of two number is = {average(a, b)}\n")

    print(f"\nResult of square root of 1st number is: {square_root(a)}")
    print(f"\nResult of square root of 2nd number is: {square_root(b)}\n")
    
    print(f"\nResult of cube root of 1st number is: {cube_root(a)}")
    print(f"\nResult of cube root of 1st number is: {cube_root(b)}\n")
    
    print(f"\nResult of factorial of 1st number is: {factorial(a)}")
    print(f"\nResult of factorial of 2nd number is: {factorial(b)}\n")
    
    print(f"\nResult of power of 1st number is: {pow(a,b)}\n")
    print(f"\nResult of power of 2nd number is: {pow(b,a)}\n")
