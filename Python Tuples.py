## What are the tuples? ##

# Tuples is collection of immutable heterogeneous python objects

# Creating a Tuples #

# emp = ()
#
# print(type(emp))
#
# print(emp)
#
# city = "Pune",
# print(type(city))
#
# city = ("Pune",)
# print(city)
#
city = ("Pune", "Mumbai", "Ahmedabad", "Delhi")
# print(city)
#
# list1 = [1, 2, 3, 4]
# tuple1 = (1, 2, 3, 4)
#
# list1.append(5)
# print(list1)

# tuple1.append(5)
# print(tuple1)

## Difference between tuples and lists ##
#
# List is mutable whereas tuples is immutable
#
# List is uses square brackets. Tuple may or may not use parentheses.

# print(city)
#
# print(city[1])
#
# print(city[-1])

# Concatination #

# num = 1, 2, 3, 4
#
# print(city + num)

# Nesting #

# nest = (city, num)
# print(nest)

# Repetiton #

# rep = ("Python", )*5
# print(rep)
#
# rep = ("Python", )
# print(rep * 5)
#
# print(rep)

# Slicing #

# print(num)
#
# print(num[1:])
#
# print(num[::-1])

# Unpacking #

# print(tuple("Simplilearn"))
#
# print(num)
#
# a, b, c, d = num
# print(a, b, c, d)
#
# a,*b,c = num
# print(a, b, c)

# Deleting a tuple #

# tuple2 = (1, 2, 3, 4, 5)
# print(tuple2)

# del tuple2

# print(tuple2)

# Built in function #

# num1 = (3, 5, 6, 6, 6, 6, 6, 7, 8, 9)
#
# print(num1.count(6))
#
# print(sum(num1))
#
# print(len(num1))
#
# print(max(num1))
#
# print(min(num1))

# Converting list to tuple #

# list1 = [1, 2, 3, 4]
#
# print(type(list1))
#
# tpl = tuple(list1)
# print(tpl)
#
# print(type(tpl))

# Nesting tuples in a list #

# list1 = [(1, 2, 3), (4, 5, 6)]
#
# print(list1)
#
# list1.append(("Tuples", "Inside", "List"))
# print(list1)
#
# list1.remove((1, 2, 3))
# print(list1)

# Nesting Lists within tuples #

# tuple1 = (["a", "b", "c"], ["d", "e", "f"])
#
# print(tuple1)
#
# tuple1[0].append('z')
# print(tuple1)
#
# tuple1[0].remove('z')
# print(tuple1)
#
# tuple1.append(['x', 'y', 'z'])
# print(tuple1)