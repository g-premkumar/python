def user_info(name, age, city) :
    '''This function prints name, age, and city
    from an argument provided to the function'''

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Janet",58, "newyork")

#if we give one arg less like below, then we will get error like:
#TypeError: user_info() missing 1 required positional argument: 'city'

#  user_info(34,"newcity")


