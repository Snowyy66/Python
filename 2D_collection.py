# 2D LIST

fruits = ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats = ["chicken","fish","mutton"]

# groceries = [fruits,vegetables,meats]

# print(meats)
# print(groceries)
# print(groceries[0])
# print(groceries[0][1])
# print(groceries[1][2])

#LIST
# groceries = [["apple","orange","banana","coconut"],
#              ["celery","carrots","potatoes"],
#              ["chicken","fish","mutton"]]

#Tupple
# groceries = ({"apple","orange","banana","coconut"},
#              {"celery","carrots","potatoes"},
#              {"chicken","fish","mutton"})

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()
    
# dialpad exercise
num_pad = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))

for x in num_pad:
    for y in x:
        print(y, end=" ")
    print()
    
    