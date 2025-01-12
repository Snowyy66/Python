# Variable Resolution - where a variable is visible & accessible
# scope resolution    - (LEGB) local > enclosed > global > Built-in


# Local
# def func1():
#     a = 1
#     print(b)
    
# def func2():
#     b = 1
#     print(a)
# func1()   
# func2()   


# enclosed
# def func1():
#     x = 1
    
#     def func2():
#         print(x)
#     func2()
# func1()


# global
# def func1():
#     print(x)
    
# def func2():
#     print(x)
    
    
# x = 3
# func1()
# func2()


# Built-in
from math import e
def func():
    print(e)
e = 6
func() 
# note - the preference of a global variable is more than built-in
