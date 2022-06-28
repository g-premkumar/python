PYTHON: started 6/23/2022

Pycharm:
keep all files in venv folder

Right click on venv --> python file (automatically saves as .py)

----------------------------------------------------------------

# single line comment

"""
This is multi line comment
type multiple lines
"""
----------------------------------------------------------------------------------------------------------------------------------
Variables:
variable are case sensitive
cars = 23
CARS = 25
CARS = 12345

print(CARS) ---> gives latest value Math


-----------------------------------------------------------------------------------------------
DataTypes:

Strings -->
single or double quotes
Immutable (operations cannot be performed)

Integers --> 
Whole numbers
Mathematical operations can be performed 


Float --> 
Fractional numbers
Mathematical operations can be performed
Python calculates places for you (no specification needed)

-------------------------------------------------------------------------------------------------

String formatting:


name = "John jacobs"
type_of_car = "Rolce royce"
school = "Foundation elementary school"

print(name +" "+ school)  --> used space in between to display nicely
print(name +" works at "+ school + ".") 
o/p: John jacobs works at Foundation elementary school.

same can be achieved using string.format()

#string formatting
#python string.format()
print("{} works at {}.".format(name,school))
o/p: John jacobs works at Foundation elementary school.

#format receives variables as args and sends them into curly braces in order

print("{} works at {} with car {}.".format(name,school,type_of_car))
o/p: John jacobs works at Foundation elementary school with car Rolce royce.

-----------------------------------------------------------------------------------

Function:

function is a unit of code that can be reused thru out a prgm

parts of function:

example:

def addition():
    a = 2            --> you can see 4 spaces after the fucntion, pycharm gives this. if you are working in cmd then give 4 spaces to make it look like this.
    b = 5                i.e All code inside a function is indented at least four spaces (one tab)
    print(a + b)
    
    
#you need to call the function to print
addition()

GEtting user input:

input("what is your name?")
#input is a python inbuilt function

def addition():
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    print(a + b)
    
addition()

#here int converts string to number


another example:
# to accept float values
def addition():
    a = int(input("enter a number. "))
    b = float(input("enter another number. "))
    print(a + b)

addition()

#note if you enter 10 & 20 in above then o/p will be float only 30.0
-----------------------------------------------------------------------
    
