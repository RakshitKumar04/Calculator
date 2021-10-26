# This is a math script where we are going to deal with all
# mathematical functionalities.
import math
import itertools  

def add(num1, num2):
    return num1 + num2


def square(num):
    return num * num


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        print("That is an invalid division, since division by 0 is not mathematically defined!")
        return "Unavailable"
    else:
        return num1 / num2


def subtract(num1, num2):
    return num1 - num2


def rmdr(num1, num2):
    rem = float(num1 % num2)
    return rem


def power(num1, num2):
    return pow(num1, num2)

def si(num1, num2):
    sn=math.asin(num1/num2)
    deg=math.degrees(sn)
    return deg

def co(num1, num2):
    sn=math.acos(num1/num2)
    deg=math.degrees(sn)
    return deg

def ta(num1, num2):
    sn=math.atan(num1/num2)
    deg=math.degrees(sn)
    return deg

def permutation():
    from itertools import permutations  
    seq = permutations(list(map(int,input("Enter the nos.: ").split())))  
    for p in list(seq):  
        print(p)

def main():
    func = int(input("Press 1 to add 2 numbers\n\
Press 2 to subtract a number from another number\n\
Press 3 to multiply 2 numbers\n\
Press 4 to divide a no. by another number\n\
Press 5 to find factorial of a number\n\
Press 6 to square a number\n\
Press 7 to to cube a number\n\
Press 8 to find square root of a no.\n\
Press 9 to find cube root of a no.\n\
Press 10 to raise a number to any power\n\
Press 11 to find remainder after division\n\
Press 12 to find average\n\
Press 13 to find percentage\n\
Press 14 to find sin value.\n\
Press 15 to find cos value.\n\
Press 16 to find tan value.\n\
Press 17 to print sample space in Permutation & Combination.\n"))

    if func <= 4:
        a = eval(input("please input 1st number: "))
        b = eval(input("please input 2nd number: "))
        if func == 1:
            print(
                f'The addition of the two numbers is: \n{a} + {b} = {add(a,b)}')
        elif func == 2:
            print(
                f'The subtraction of the two numers is: \n{a} - {b} = {subtract(a,b)}')
        elif func == 3:
            print(
                f'The multiplication of the two numbers is: \n{a} x {b} = {multiply(a,b)}')
        else:
            print(f'The division results in: \n{a} / {b} = {divide(a,b)}')
    elif func < 10:
        num = eval(input('Enter the number: '))
        print(
            f'The factorial of {num} = {math.factorial(num)}' if func == 5 else '')
        print(f'The square of {num} = {power(num,2)}' if func ==
              6 else f'The cube of the {num} = {power(num, 3)}' if func == 7 else '')
        l = math.sqrt(
            abs(num)) if func == 8 else math.pow(
            abs(num), 1 / 3) if func == 9 else ''
        print(f'The cube root of {num} is {l}' if func ==
              9 else f'The square root of {num} is +{l} or -{l}' if func == 8 else '')
    elif func == 10:
        num = eval(input('Enter no. to find the power of: '))
        e = eval(input('Enter the value of the power: '))
        print(f'The no. {num} to the power{e}: {num}^{e}= {power(num, e)}')
    elif func == 11:
        a = eval(input('Input no. being divided(dividend): '))
        b = eval(input('Input the divisor: '))
        if not b == 0:
            rem = rmdr(a, b)
            print(f'{a} / {b} gives remainder as {rem}')
        else:
            print('error: division by zero is undefined.')
    elif func == 12:
        nums = int(
            input('Enter the no. of terms you want to find the average of: '))
        num_list = [eval(input(f'Enter term#{_+1}: ')) for _ in range(nums)]
        print(f"Average of {','.join(map(str, num_list))} is: {math.sum(num_list)/nums}")
    elif func == 13:
        n = eval(input('Enter the value of specific parts: '))
        d = eval(input('Enter the total value: '))
        if not d == 0:
            print(f'\nThe percentage is equal to- {(n/d)*100}%')
        else:
            print('error: division by zero is undefined.')
    elif func == 14:
        opp = eval(input('Enter the height of right angle triangle : '))
        hyp = eval(input('Enter the hypotenuse of right angle triangle : '))
        sum=si(opp,hyp)
        print(format('Sin θ = {:.0f}'.format(sum) +'°'))
    elif func == 15:
        opp = eval(input('Enter the base of right angle triangle : '))
        hyp = eval(input('Enter the hypotenuse of right angle triangle : '))
        sum=co(opp,hyp)
        print(format('Cos θ = {:.0f}'.format(sum) +'°'))
    elif func == 16:
        opp = eval(input('Enter the height of right angle triangle : '))
        hyp = eval(input('Enter the base of right angle triangle : '))
        sum=co(opp,hyp)
        print(format('Tan θ = {:.0f}'.format(sum) +'°'))
    elif func == 17:
        permutation()

if __name__ == '__main__':
    """Main function which is going to drive whole program"""
    print(f'\n\n* Hi, welcome to my program hope you have a good time\n\n')  # Press Ctrl+F8 to toggle the breakpoint.
    main()