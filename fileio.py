# # reading a file
# f = open("demo.txt", "r")
# # data = f.read()
# line1 = f.readline()
# line2 = f.readline()
# print(line2)
# # print(type(data))
# f.close()


# writing a file
# f = open("demo.txt", "w")
# f.write("i want to learn javascript")
# f.write("\nThen i will move to react js")
# f.close()



# Overwrite(r+)
# f = open("demo.txt", "r+")
# f.write("abc")
# f.close()


# W+
# f = open("demo.txt", "r+")
# print(f.read())
# f.write("abc")
# f.close()


# a+
# f = open("demo.txt", "a+")
# print(f.read())
# f.write("abc")
# f.close()


# with-syntax(another method of reading/writing a file)
# with open ("demo3.txt", "r") as f:
#     data = f.read()
#     f.close()
# print(data)



# import a module
# import os
# os.remove("demo2.txt")


# practice -> (1) - create a new file "practice.txt" using python. Add the following data in it
#            Hi everyone , 
#            we are learning file I/O 
#            using python 
# f = open("practice.txt", "w")
# data = f.write("Hi everyone,\n we are learning file I/O\n using python")
# print(data)
# f.close()

# (2) - now, WAF that will replace "python" with "java"

# with open ("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("python", "java") 
# print(new_data)
# with open ("practice.txt", "w") as f:
#     data = f.write(new_data)

# (3) - now search the word "learning" exits or not
# with open ("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find("learning") != -1):
#         print("found")
#     else:
#         print("Not found")
        
        
        
        
        
# practice 2 - WAF to find in which line of the file does the word "learning" occur first.
#              print -1 if word not found
def check_for_line():
    word = "learning"
    data = True
    line_number = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_number)
                return
            line_number += 1
    return -1
check_for_line()