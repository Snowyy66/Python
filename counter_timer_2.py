import time
my_time = int(input("enter the time in seconds : "))
print("Hurry up")
for x in reversed(range(0,my_time)):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
print( "BOOMMM....💥💥💥")