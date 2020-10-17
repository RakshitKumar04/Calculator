# This is a math script where we are going to deal with all
# mathematical functionalities.

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
    a = int(input("please input 1st number: "))
    b = int(input("please input 2nd number: "))
    print(f"\nResult of factorial of 1st number is: {fact(a)}\n")
    print(f"\nResult of factorial of 2nd number is: {fact(b)}\n")