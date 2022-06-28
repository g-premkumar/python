def add(*args):
    print(sum(args))

add(2, 3, 4)
add(2, 6, 8, 184)
########################

def application(**kwargs):
    print(kwargs)


application(name="Jess", email="mail@mail.com")
application(name="Susan", surname="Johnson", age=42)

#########################
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email), args, kwargs)
    print(args)
    print(kwargs)


application("Jess", "Ingrass", "mail@mail.com", "TeachCode.org" ,75000 , hire_date = "September 2010")