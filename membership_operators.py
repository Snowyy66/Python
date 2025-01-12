# membership_operators - used to test whether a value or varibale is found in a sequence 
#                        (string, list, tuple, set, dictionary)
#                        1.in 
#                        2.Not in

# word = "APPLE"
# letter = input("Guess a letter in the secret word : ") 

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")
    
    
    
# students = {"nolan", "fincher", "tarantino"}

# student = input("Enter the name of student : ") 

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")


email = input("type your email : ")
if "@" in email and "." in email:
    print("valid email")
else:
    print("Not a valid email")