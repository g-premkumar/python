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

operation = input("Please choose +, -, *, or / ")
if operation == '+':
    add()
elif operation == '-':
    substraction()
elif operation == '*':
    multiply()
elif operation == '/':
    divide()
else :
    print ("please enter any valid operator")

"""
add()
substraction()
multiply()
divide()
"""