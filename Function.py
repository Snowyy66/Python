# def happy_birthday():
#     print("Happy birthday to you !")
#     print("you are 18 old")
#     print("Happy birthday to you !")

# happy_birthday()
# happy_birthday()
# happy_birthday()


# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"you are {age} years old !")
#     print("Happy birthday to you !")
#     print()

# happy_birthday("Bro", 20)
# happy_birthday("ashish", 17)
# happy_birthday("john", 19)


# return = a statement used to end a function and send a result back to caller
# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiplication(x, y):
#     z = x * y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiplication(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("ashish", "sisodiya")
print(full_name)