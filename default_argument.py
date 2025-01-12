# default arguments = a default value for certain parameter
#                     default is used when that argument is omitted 
#                     make your functions more flexible, reduces # of argumnets
#                     1. positional, 2. DEFAULT 3. keyword 4. arbitrary

# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500,0,0.05))



# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))



#Exercise
import time

# def count(start,end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
# count(0,10) 

def count(end,start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")
count(10) 