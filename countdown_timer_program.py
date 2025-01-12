import time
# time.sleep(3) 
# print("TIME'S UP !")
#3 sec baad result print hoga



my_time = int(input("enter the time in seconds : "))
for x in reversed(range(0,my_time)):
# for x in (range(my_time,0,-1)):
# another technique for reverse (line-10)
    time.sleep(1)
    print(x)
print( "....HAPPY DIWALI....💥💥💥")