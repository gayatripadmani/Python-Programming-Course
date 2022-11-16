# from os import path
#
# def createfile(dest):
#     if not (path.isfile(dest)):
#         f = open(dest, 'w')
#         f.write("Welcome to Python Scripting")
#         f.close()
#
# dest = "C:\\Users\\Gayatri\\PycharmProjects\\Simplilearn Python Course\\sample.txt"
#
# createfile(dest)
# input("File Created")

# def fun1(*args):
#     for i in args:
#         print(i)
#
# fun1(10, 20, 30, 40, 50, 'abcdef')


# def fun1(*args, **kwargs):
#     for i in kwargs.items():
#         print(i)
#
# fun1(a = 10, b = 20, c = 30, d = 40, e = 50)


# def fun1():
#     x = 10;
#     def fun2(x):
#         return x + 1
#     return fun2(x)
#
# result = fun1()
# print(result)


# def fun1(called_fun):
#     print("This is the first function")
#
#     def nested_fun1(called_fun):
#         print("This is the nested function")
#         called_fun()
#     return nested_fun1(called_fun)
#
# def outer_fun1():
#     print("This is the Outer function")
#
# obj = fun1(outer_fun1)


#factory

# B = type("BaseClass", (object,), {})
# c1 = type("c1", (B, ), {'val':5})
# c2 = type("c2", (B, ), {'val':10})
#
# def ClassCreator(bool):
#     if bool:
#         return c1()
#     else:
#         return c2()
#
# print(ClassCreator(True).val)
# print(ClassCreator(False).val)


def fun1(called_fun):
    print("This is the first function")

    def nested_fun1(called_fun):
        print("This is the nested function")
        called_fun()
    return nested_fun1(called_fun)

@fun1
def outer_fun1():
    print("This is the Outer function")

outer_fun1()