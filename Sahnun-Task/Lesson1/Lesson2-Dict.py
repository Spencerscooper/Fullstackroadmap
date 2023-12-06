#Question: Declare a dictionary with keys as "names and ages as values,
#then loop through all the keys and value and print them as "key:{key},
# value, {value}

bio = {"Spencer": 5, "Sahnu":3, "Jeff" : 2, "Freena": 1}

search = bio.items()
for names in search:
    print(type(search))
    print(names)

# Question write a program that takes in an aray of integers and print out each
# integer squared to the second power)


#def print_squared(numbers):
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    square = number ** 2
    print(f"The square of\t {number} \t {square}")



