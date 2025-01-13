# Del keyword

# class student:
#     def __init__(self, name):
#         self.name = name

# s1 = student("Ashish")

# # del s1
# # print(s1)

# print(s1.name)
# del(s1.name)
# print(s1.name)


# Private attributes and methods
# They are meant to be used only within the class and are not accessible from outside the class

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         # self.acc_pass = acc_pass #public
#         self.__acc_pass = acc_pass #private
    
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# # print(acc1.acc_pass) #public
# # print(acc1.__acc_pass) #private
# # it(line 30) will print nothing bcoz now it's private
# # To print, we need to define and call a function inside the class(line 26 & 36 )
# print(acc1.reset_pass())


# Inheritance
# When one class (child/derived) derives the properties & methods of another class(parent/base).

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("pirus")

# print(car1.name)


# Property - We use property decorator on any method in the class to use the method as a property.
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy 
        self.chem = chem 
        self.math = math 
        self.percentage = str((self.chem + self.phy + self.math) / 3) + "%"
    
    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    # now we use property decorator
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 88
# print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage)
