# collection = single "variable" used to store multiple values
# list = [] order & changeable. duplicates ok
# set =  {} unorder & immutable, but add/remove ok. No duplicates
# tuple = () order & changeable, duplicates ok. faster


# 1. LIST
# fruits = ["apple","banana","orange","grapes"]

# print(fruits[0])

# print(fruits[0:3])

# print(fruits[0::3])

# print(fruits[:3])

# for x in fruits:
#     print(x)


# print("pineapple" in (fruits))


# fruits[0] = "pineaapple"
# for x in fruits:
#     print(x)


# fruits[1] = "pineaapple"
# for x in fruits:
#     print(x)

# fruits.append("pineapple") # append use for adding at last/end
# fruits.remove("banana") # remove use for removing element
# fruits.insert(2,"pineapple")
# fruits.reverse() #reverse orginal order
# fruits.sort() #alphabetically
# fruits.clear()
# print(fruits.index("banana")) #for returning index
# print(fruits.count("banana")) #How many banana
# print(fruits)



# 2. SET
# fruits = {"apple","banana","orange","grapes"}

# print(fruits) #after every printing order will change
# print(len(fruits))
# print("pineapple" in fruits)
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() #remove any element
# fruits.clear() 
# fruits = {"apple","banana","orange","grapes","grapes"} # ek baar hi ayega grapes
# print(fruits)


# 2. SET
fruits = ("apple","banana","orange","grapes")
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("apple"))
print(fruits.count("apple"))
print(fruits)







# note - all three has almost same use but different benefits