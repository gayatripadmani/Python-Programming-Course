## NumPy Libarary ##

## What is NumPy? #

# NumPy is the core library for scientific and numerical computing in python

# It provides high-performance multidimensional array object and tools fir working with arrays.

# In NumPy, dimensions are called axes.

# One dimensional array: 0 1 2 3 4 5   shape(6)

# Two dimensional array: shape(2,4)

## Installing and importing Numpy #

# jupyter.org and anaconda.com

## NumPy Array #

## NumPy Array vs Python list #

# why should we use NumPy array when we have python list? --- -Fast -Convenient -Less Memory

## Basics of NumPy #

import numpy as np
# a = np.array([1,2,3])
# print(a)
# print(a[0])

## Finding size and shape of any array #

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)
# print(a.ndim)
# print(a.itemsize)
# print(a.shape)

# a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
# print(a)
# print(a.itemsize)
# print(a.shape)

# a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.complex_)
# print(a)

# a = np.zeros((3, 4))
# print(a)

# a = np.ones((3, 4))
# print(a)

# l = range(5)
# print(l)

# l = np.arange(5)
# print(l)

## Range and arange functions #

import time
import sys
# b = range(1000)
# print(sys.getsizeof(5) * len(b))

# c = np.arange(1000)
# print(c.size * c.itemsize)

# size = 100000
# l1 = range(size)
# l2 = range(size)
# A1 = np.arange(size)
# A2 = np.arange(size)
# print(size)
# print(l1)
# print(l2)
# print(A1)
# print(A2)

# start = time.time()
# result = [(x + y) for x,y in zip(l1, l2)]
# result = [(x + y) for x,y in zip(l1, l2)]
# print(result)
# print("Python list took:", (time.time() - start) * 1000)

# result = A1 + A2
# print("NUmPy list took:", (time.time() - start) * 1000)

## NumPy string functions #

# print("Concantation Example")
# print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))
# print(np.char.multiply('hello ', 3))
# print(np.char.center('hello ', 20, fillchar= '-'))
# print(np.char.capitalize("hello world"))
# print(np.char.title("hello.. how are you?"))
# print(np.char.upper(["python", "data"]))
# print(np.char.lower(["PYTHON", "DATA"]))
# print(np.char.splitlines("hello\nhow are you?"))
# print(np.char.strip(["nain", "admin", "anaita"], "a"))
# print(np.char.join([":", "-"], ["dmy","ymd"]))
# print(np.char.replace("He is good dancer", "is", "was"))