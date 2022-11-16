## Python Dictinoaries Sets ##
#
# Dictionaries is an unordered collection of data stored as a pair of key and value.
#
# Syntax:
# variable_name = (key1:value1, key2:value2,...}
#

# Creating Dictionsries #

# d1 = {}
# print(type(d1))

# d1 = {1:"Welcome", 2:"to", 3:"My", 4:"World"}
# print(d1)

# d2 = {"Name":"Gayatri", "Age":20, "Profession":"Student"}
# print(d2)

# d3 = dict([(1,"Welcome"), (2,"to"), (3,"My"), (4,"World")])
# print(d3)

# d4 = {"Name":{"First Name": "Gayatri", "Last Name":"Padmani"}, "Age":20, "Profession":"Student"}
# print(d4)

# Adding Element #

# d = {}
# d[0] = "Welcome"
# print(d)

# d = {}
# d["Name"] = "Gayatri"
# print(d)

# d = {}
# d["Name"] = {"First Name": "Gayatri", "Last Name":"Padmani"}
# print(d)

# Accessing Element #

# print(d)
#
# print(d["Name"])
#
# print(d["Name"]["First Name"])
#
# print(d1.get(1))

# Deleting Element #

# print(d1)

# d1.pop(1)
# print(d1)

# d1.popitem()
# print(d1)

# Using Built in functios #

# d1.values()
# print(d1)

# keys = {'a', 'b', 'c', 'd'}
# value = 1
# d2 = dict.fromkeys(keys,value)
# print(d2)
#
# d2.clear()
# print(d2)
#

## Set In Python ##
#
# Set in an unordered collection of unique elemenet
#
# Syntax:
#
# variable_name = set(['a', 'b', 'c', 'd'])
#

# Sets #

# s = set([1, 2, 3, 4])
# print(s)
# print(type(s))

# s.add('a')
# print(s)

# fs = frozenset([1, 2, 3, 4,])
# print(fs)
# fs.add('a')
# print(fs)

s1 = set([1, 3, 7, 2])
s2 = set([3, 2, 8, 9])

print(s1)
print(s2)

# s1.union(s2)
# print("Union Method: ", s1)

# s1.intersection(s2)
# print("Intersection Method: ", s1)