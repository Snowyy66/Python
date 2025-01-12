# execute code wwhile some comdition remains true

# name = input("Type your name : ")
# while name == "":
#     print("you didn't enter your name")
#     name = input("Type your name : ")
# else:
#     print(f"Hello {name}")


# age = int(input("Type your age : "))
# while age < 0:
#     print("your age can't be in negative")
#     age = int(input("Type your age : "))
# else:
#     print(f"you are {age} years old")


food = (input("Enter a food you like(q to quit) : "))
while not food == "q":
    print(f"you like {food}")
    food = (input("Enter a food you like(q to quit) : "))
print("bye")


# number = int(input("Enter a number : "))
# while number < 1 or number > 10:
#     print(f"your {number} is not valid")
#     number = int(input("Enter a number : "))
#     print(f"your number is {number}")