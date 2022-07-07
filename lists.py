fruits = ["peaches","apples","oranges"]
year = [3, "1998", 2.5, 987, "1994"]

print(fruits, year)

fruits.append("oranges") #append is a function to add
print(fruits)

fruits.extend(year) #here we are extending another list(year) with fruits
print(fruits)

fruits.remove("oranges")

print(fruits)

fruits.pop(0)

print(fruits)

fruits.pop(-1)
print(fruits)

#fruits.sort()
#print(fruits)

numbers = [5,1928,4, 17,68,7.5, 67.8, 99]
numbers.sort()
print(numbers)

print("apple" in fruits)

print("apples" in fruits)

fruits.append("apples")
print(fruits)
print(fruits.count("apples"))

print(fruits.count("apple"))

print(fruits.index("apples"))