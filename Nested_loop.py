# Nested loop - loop within another loop

# for x in range(1,11):
#     print(x, end="-")


for x in range(3): # execute three times(total 30 numbers)
    for y in range(1,11):
        print(y, end="_")
   
   
# for x in range(3): 
#     for y in range(1,11):
#         print(y, end="")
#     print()



# rows = int(input("Enter the number of rows : "))
# columns = int(input("Enter the number of columns : "))
# symbol = input("Enter the symbol : ")
# for x in range(rows): 
#     for y in range(columns):
#         print(symbol, end="")
#     print()