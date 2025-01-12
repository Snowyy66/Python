# AND OR NOT

# temp =  35
# is_raining = False

# if temp > 35 or temp < 0 or is_raining :
#     print("The outdoor event is canceled")
# else:
#     print("The outdoor event is still scheduled")
    
    
# temp =  35
# is_raining = True

# if temp > 35 or temp < 0 or is_raining :
#     print("The outdoor event is canceled")
# else:
#     print("The outdoor event is still scheduled")

temp = float(input("Enter the temperature "))
if temp > 35 and temp < 10:
    print("The outdoor event is cancelled")
    
else:
    print("The outdoor event is scheduled")