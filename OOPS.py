# # Class
# class Student:
#     name = "Ashish Sisodiya"
# # creating object(instance of class)
# s1 = Student()
# print(s1.name)


# class car:
#     color = "blue"
#     brand = "mercedes"
# car1 = car()
# print(car1.color)
# print(car1.brand)



# init function - All class have a function called _init_(), which is 
#                 always executed when the object is being initiated
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class

# class Student:
#     name = "anonymous" # class attributes
#     def __init__(self, name, marks):
#         self.name = name # object attributes, precedance (obj>class)
#         self.marks = marks

# s1 = Student("ashish",97)
# print(s1.name,s1.marks)
# s2 = Student("karan",98)
# print(s2.name,s2.marks)



# Methods - methods are function that belong to objects
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#     def welcome(self):
#         print("Welcome student")
# s1 = Student("karan",98)
# s1.welcome()


# Practice - create student class that take name & marks of 3 subjects as arguments
#            in constructor 
#            Then create a method to print the average

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi,",self.name,"your average score is : ",sum/3)
          
# s1 = Student("Ashish",[98,99,100])
# s1.get_avg()


# static method or Important terms - methods that don't use self parameter(work at class level)
# 1.Abstraction - show essential features of the class.
# 2.Encapsulation - Wrapping data and functions into a single unit(object).

# practice - create account class with 2 attributes  - balance & account number
#            create methods for debit, credit & printing the balance
class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc
        
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("Total balance is : Rs. ", self.get_balance())
    
    # credit method   
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount, "was credited")
        print("Total balance is : Rs. ", self.get_balance())   
        
    def get_balance(self):
        return self.balance
      
acc1 = account(10000, 926232341)
print("your account balance is :",acc1.balance)
acc1.debit(300)
acc1.credit(400)
