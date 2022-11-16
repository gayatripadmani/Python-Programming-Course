## Threding in Python ##

# Process #

# A process is an executable instance of a computer program

# Thread #

# A thread is a sequence of instruction in a program that can e executed independently of the remaining program

# from threading import *
# def show():
#     print("This is a child thread")
# t = Thread(target= show())
# t.start()
# print("This is parent thread")

# from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in  range(5):
#             print("\nThis is a child class")
# t = MyThread()
# t.start()
# for i in range(5):
#     print("\nThis is th main thread")

# from threading import *
# class Demo:
#     def show(self):
#         for i in range(5):
#             print("This is the child thread")
# obj = Demo()
# t = Thread(target=obj.show())
# t.start()
# for i in range(5):
#     print("This is parent Thread")

# Context Switching #

# Storing the state of a process or thread and resuming its execution at a later time is called context switching.

# Multithreading #

# A model where multiple threads within a process execute independently while sharing the same resources is called multithreading


# import time
# from threading import *
# class Demo:
#     def num(self):
#         for i in  range(1,6):
#             print("The number is", i)
#             time.sleep(1)
#         print("\n")
#     def double(self):
#         for i in range(1,6):
#             print("The double of the number", 2*i)
#             time.sleep(1)
#         print("\n")
#     def square(self):
#         for i in  range(1,6):
#             print("This square os the number", i*i)
#             time.sleep(1)
#         print("\n")
# obj = Demo()
# t1 = Thread(target=obj.num())
# t2 = Thread(target=obj.double())
# t3 = Thread(target=obj.square())
#
# t1.start()
# time.sleep(0.2)
# t2.start()
# time.sleep(0.2)
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("This is main thread")