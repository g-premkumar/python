def user_info(name, age=0, city='Tucson') :
    '''This function prints name, age, and city
    from an argument provided to the function'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Samuel",58, "newyork")
user_info("John")
user_info(age=56, name = "kadeem")