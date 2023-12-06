# datatype int, float, complex, bool, bytearray, bytes, memoryview, NoneType, range
#Ok, sounds good. Well, you did fantastic today. I'm happy with your progress, and you should be too. For homework, I want you to research the difference between compiled and interpreted languages. Also, if there's time, look into binary an octal notation
#<shmohamud> Absolutely, get some sleep, you earned it. Tomorrow same time?

my_dict = {
    "Spencer": 87,
    "Freena": 99,
    "Shallon": 100,
    "Shanun": 97,
}
print(my_dict)


new_dict = my_dict.items()
print(new_dict)

def hello_world(name):
    print(f"Hello {name}")

hello_world("Sahnun")

counter = 0

while counter < 100:
    counter = counter + 1

    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)

counter = 0

while counter < 50:
    counter += 1
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 5 == 0:
        print("Buzz")
        
    elif counter % 3 == 0:
        print("Fizz")

    else:
        print(counter)

#In Python these symbol are consider the official comparising operator: == < > >= <= !=. So
# Can I consider this string method to be a comparison operators too (startswith and endswith)?

first_name = "Spencer"
last_name = "Cooper"
print(first_name.startswith("S"))
print(last_name.endswith("r"))

