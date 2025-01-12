# DICTIONARIES
# info = {
#     # "key" : "values",(can't be write two keys with same name)
#     "Name" : "Ashish Siodiya",
#     "Subjects" : ["python","java","javascipt"],
#     "college" : "AEC agra",
#     "cgpa" : 9.9
# }
# info["Name"] = "ellipse"
# print(info)
# print(type(info))


# Nested Dictionary
# student = {
#     "name" : "walter white",
#     "score" : {
#         "chem" : 100,
#         "phy" : 0,
#         "maths" : 0
#     } 
# }
# print(student["score"])
# print(student["score"]["chem"])

# Dictionary methods
# print(student.keys())
# print(student.values())
# print(student.items()) # return as tuple
# student.update({"city" : "agra"})
# print(student)
# Type casting(to tupple)
# print(list(student.keys()))
# print(len(list(student.keys())))

# SETS - immutable , element must be unique and it stores them in unordered manner
# collection = {1,2,3,4,3}
# set ignores duplicate values
# print(collection)
# print(type(collection))


# collection = set() # empty set
# print(collection)
# print(type(collection))

# set methods
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(8)
# collection.add("hello bro")
# collection.remove(2)
# collection.clear()
# print(collection.pop())  # random order me elements pop ho jayenge
# print(collection.pop())  
# print(collection)

set1 = {1,2}
set2 = {5,2}
print(set1.union(set2))
print(set1.intersection(set2))
