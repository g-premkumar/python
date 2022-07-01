#Break
temp_f = 40
while temp_f > 32:
    print("the water degrees is {} .".format(temp_f))
    temp_f -= 1
    if temp_f == 36:
        break

#Continue
for number in range(1,11):
    if number == 7:
        print("we are skipping number 7.")
        continue
    print("this is number {}.".format(number))

#Pass
for number in range(1,11):
    if number == 3:
        pass
    else:
        print("this is number {}.".format(number))