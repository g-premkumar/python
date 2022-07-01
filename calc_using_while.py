#Calc prgrm executing once and ended
# so to give user another chance to enter we can use while

on = True


def add():
    a = float(input("enter a number. "))
    b = float(input("enter another number. "))
    print(a + b)

def substraction():
    a = float(input("enter a number. "))
    b = float(input("enter another number. "))
    print(a - b)

def multiply():
    a = float(input("enter a number. "))
    b = float(input("enter another number. "))
    print(a * b)

def divide():
    a = float(input("enter a number. "))
    b = float(input("enter another number. "))
    print(a / b)

#make sure to provide correct indentent in below code to not get error
while on:
    operation = input("Please choose +, -, *,/ or q ")  #q is added to quit
    if operation == '+':
        add()
    elif operation == '-':
        substraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else :
        print ("please enter any valid operator")

"""
add()
substraction()
multiply()
divide()
"""