# Dictionary - A collection of {key : value} pairs , order & changeable. No duplicates

capitals = {"USA" : "Washinghton D.C",
            "INDIA" : "New delhi",
            "china" : "Beijing",
            "South korea" : "Seol"}

# print(capitals.get("china"))

# if capitals.get("africa"):
#     print("That capital exists")
# else:
#         print("That capital doesn't exists")


# capitals.update({"Germany" : "Berlin"})
# print(capitals.get("Germany"))

# capitals.update({"USA" : "agra"})
# print(capitals.get("USA"))

# capitals.pop("china")
# it will remove china
# print(capitals)

# capitals.popitem()
# remove the latest one
# print(capitals)

# capitals.clear()
# remove all
# print(capitals)

# keys = capitals.keys()
# for key in capitals.keys():
#      print(key)


for key, value in capitals.items():
    print(f"{key} : {value}")
