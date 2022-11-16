## MatPlotlib Library ##

# What is MatPlotlib? #

# It is an open source drawing library which supports rich drawing types.

# It is used to draw 2D and 3D graphics.

# You can understand your date easily by visualizing it with the help of matplotlib!

# You can generate plots, histograms, bar charts and many other charts with just a few lines of code

# Types of Plots #

# Bar Chart
# Scatter Plot
# Pie Chart
# Histogram
# Line Chart
# Area Graph

# What is MatPlotlib? #

# Let's Start Plotting them...

## MATPLOTLIB Tutorial

from matplotlib import pylab

# print("Version: ", pylab.__version__, "\n")

# """ Use NumPy to generate random data """

import numpy as np

# x = np.linspace(0, 10, 25)
# y = x * x + 2
# print(x, "\n")
# print(y, "\n")
# print(np.array([x, y]).reshape(25, 2), "\n")

# """ It only takes 1 command to draw """

# pylab.plot(x, y, 'r') # 'r' stands for red
# print(pylab)

""" Drawing a subgraph """

# pylab.subplot(1, 2, 1)  # The contents of brackets represent (rows, columns, indexes)
# pylab.plot(x, y, 'r--')  #The third parameter here determines color and line styles
# pylab.subplot(1, 2, 2)
# pylab.plot(y, x, 'g*-')
# print(pylab)

# (1, 2, 1) and (1, 2, 2) are signoficont if we want tiled subplots, without both the graphs will in the same plot

# for example

# pylab.subplot(1, 2, 1)  # The contents of brackets represent (rows, columns, indexes)
# pylab.plot(x, y, 'r--')  #The third parameter here determines color and line styles
# pylab.subplot(1, 2, 1)
# pylab.plot(y, x, 'g*-')

## Operator Description

# fig, add_axes() = Intializes subplot a = fig.add_subplot(222)

# fig, b = plt.subplots(nrows=3, ncols=2) = Adds subplot

# ax = plt.subplots(2,2) = crates subplot

from matplotlib import pyplot as plt

# fig = plt.figure()
# axis = fig.add_axes([0.5, 0.1, 0.8, 0.8]) # Control the left, right, width, height of the canvas (from 0 to 1)
# axis.plot(x, y, 'r')

# again we can draw subgraphs

# fig, axes = plt.subplots(nrows = 1, ncols = 2) # submap is of 1 row, 2 columns
# for ax in axes:
    # ax.plot(x, y, 'r')

# we can also draw a picture, or graph, inside another grah

# fig = plt.figure()

# Control the left, right, width, height of the canvas (from 0 to 1)

# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  #big axes
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  #small canvas

# axes1.plot(x, y, 'r')
# axes2.plot(y, x, 'g')

# fig = plt.figure(figsize=(16,9), dpi=100) #New graphics object

# fig.add_subplot()

# plt.plot(x, y, 'r')


# fig, axes = plt.subplots()

# axes.set_title("title")

# axes.plot(x, y, 'r')

# fig, axes = plt.subplots()

# axes.set_xlabel("x - label")
# axes.set_ylabel("y - label")

# axes.set_title("Title")

# axes.plot(x, y, 'r')


# ax.legend(["label1", "label2"])

# fig, axes = plt.subplots()
# axes.set_xlabel("x - label")
# axes.set_ylabel("y - label")

# axes.set_title("title of graph")

# axes.plot(x, y**2)
# axes.plot(x, x**3)

# axes.legend(["y = x**2", "y = x**3"], loc=2)


# In Matplotlib, you can set other properties such as line color, transparancy, and more.

# fig, axes = plt.subplots(dpi = 150)

# axes.plot(x, x**2, color='red', alpha=.5)
# axes.plot(x, x+2, color="#1555dd", alpha=.5)
# axes.plot(x, x+3, color="green", alpha=.5)


# fig, axes = plt.subplots(dpi = 100)

# Line width
# axes.plot(x, x+1, color='blue', linewidth=0.25, linestyle='-')
# axes.plot(x, x+2, color='blue', linewidth=1)
# axes.plot(x, x+3, color='blue', linewidth=1.5)
# axes.plot(x, x+4, color='blue', linewidth=2)


# fig, ax = plt.subplots(dpi = 100)

# Line width
# ax.plot(x, x+1, color='blue', linewidth=2, linestyle='-')
# ax.plot(x, x+2, color='blue', linewidth=2, linestyle='-.')
# ax.plot(x, x+3, color='blue', linewidth=2, linestyle=':')

# line, =ax.plot(x, x+4, color="black", linewidth=1.50)
# line.set_dashes([5, 10, 15, 10])

# line, =ax.plot(x, x+5, color="black", linewidth=1.50)
# line.set_dashes([5, 10, 15, 3])

# line, =ax.plot(x, x+6, color="black", linewidth=1.50)
# line.set_dashes([5, 10, 4, 10])


# fig, ax = plt.subplots(dpi = 100)

# Line width
# ax.plot(x, x+1, color='blue', marker='o')
# ax.plot(x, x+2, color='blue', marker="+")
# ax.plot(x, x+3, color='blue', marker="s")
# ax.plot(x, x+4, color='blue', marker="1")

# ax.plot(x, x+5, color='blue', marker='o', markersize=5)
# ax.plot(x, x+6, color='blue', marker="s", markerfacecolor='red')
# ax.plot(x, x+7, color='blue', marker="o", markersize=15, markerfacecolor='green')


# """ Set the canvas grid and axis range """

# fig, axe = plt.subplots(1, 2, figsize=(10,5))

# axe[0].plot(x, x**2, x, x**3, lw=2)
# axe[0].grid(True)

# axe[1].plot(x, x**2, x, x**3, lw=2)
# axe[1].set_ylim([0,60])
# axe[1].set_xlim([2,5])
# axe[1].grid(True)


## Other 2D Graphics

# n = np.array([0, 1, 2, 3, 4, 5])

# fig, a = plt.subplots(1, 4, figsize=(16, 5))

# a[0].set_title("scatter")
# a[0].scatter(x, x+0.25*np.random.randn(len(x)))

# a[1].set_title("step")
# a[1].step(n, n**2, lw=2)

# a[2].set_title("bar")
# a[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)

# a[3].set_title("fill_between")
# a[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)


# """ Draw a rader chart """

# fig = plt.figure(figsize=(6,6))
# ax= fig.add_axes([0.0, 0.0, .6, .6], polar=True)
# t = np.linspace(0, 2*np.pi, 100)
# ax.plot(t, t*.2, color='blue', lw=3)


# """ Draw a rader chart """

# fig = plt.figure(figsize=(6,6))
# ax= fig.add_axes([0.0, 0.0, .6, .6], polar=True)
# t = np.linspace(0, 2*np.pi, 100)
# ax.plot(t, t*.2, color='blue', lw=3)


# Draw cantour image

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# delta= 0.025
# x = np.arange(-3.0, 3.0, delta)
# y = np.arange(-2.0, 2.0, delta)
# X, Y = np.meshgrid(x, y)
# z1 = np.exp(-X**2 -Y**2)
# z2 = np.exp(-(x - 1)**2 - (Y - 1)**2)
# z = (z1 - z2) * 2

# print(X)
# print(Y)


# fig, ax = plt.subplots()
# cs = ax.contour(x, y, z)
# ax.clabel(cs, inline=1, fontsize=10)
# ax.set_title('contour map')