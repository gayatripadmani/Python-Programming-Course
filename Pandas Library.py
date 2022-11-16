## Pandas Library ##

# What is Pandas? #

# Pandas is a tool for data processing which helps in data analysis.

# It provides functions and methods to efficiently manipulate large datasets


# Pandas Series #

# Series is a one-dimensional array ith labels. It can contain any data type including integers, strings, floats, python objects and more

# index         Data
# 1             'A'
# 2             'B'
# 3             'C'


# Basic Operations on series #

## Pandas Tutorial

import pandas as pd

# check pandas version
# print("Version of Pandas: ", pd.__version__, "\n")

## Series create, manipulate, querry, delete

# creating a series from alist
# print("Series of Pandas: \n")
# arr = [0, 1, 2, 3, 4]
# s1 = pd.Series(arr)
# print(s1, "\n")

# order = [1, 2, 3, 4, 5]
# s2 = pd.Series(arr, index=order)
# print(s2, "\n")

import numpy as np

# n = np.random.randn(5)  #Create a random Ndarray
# index = ['a', 'b', 'c', 'd', 'e']
# s3 = pd.Series(n, index=index)
# print(s3, "\n")

# create series from dictionary
# d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# s4 = pd.Series(d)
# print(s4, "\n")

# you can modify the index of series
# print(s1)
# s1.index = ['A', 'B', 'C', 'D', 'E']
# print(s1, "\n")

# Slicing
# print(s1[:3], "\n")

# Append
# s5 = s1.append(s4)
#  print(s5)

# Drop
# print(s4.drop('e'))

## Series Operations

# a1 = [0, 1, 2, 3, 4, 5, 7]
# a2 = [6, 7, 8, 9, 5]

# print(pd.Series(a2), "\n")
# print(pd.Series(a1), "\n")
# print(s5.add(s4), "\n")
# print(s5.sub(s4), "\n")
# print(s5.mul(s4), "\n")
# print(s5.div(s4), "\n")
# print("median", s4.median(), "\n")
# print("max", s4.max(), "\n")
# print("min", s4.min(), "\n")


# Pandas DataFrame #

# DataFrame is a two-dimensional data structure with labels. we can use label to locate data

# Column index(df.columns)
# Series of data
# Row index (df.index)


# Basic operations on dataframe #

## Create DataFrame

# datas = pd.date_range('today', periods=6)  # Define time sequence as index
# print(datas, "\n")

# n_arr = np.random.randn(6,4)  # Import numpy random array
# print(n_arr, "\n")

# col = ['A', 'B', 'C', 'D']  # Use the table as the column name
# df1 = pd.DataFrame(n_arr, index=datas, columns=col)
# print(df1, "\n")

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = pd.DataFrame(data, index=labels)
# print(df2, "\n")

# See datatypes of array
# print(df2.dtypes, "\n")
# print(df2.head(), "\n")
# print(df2.tail(), "\n")
# print(df2.tail(3), "\n")
# print(df2.index, "\n")
# print(df2.index, "\n")
# print(df2.columns, "\n")
# print(df2.values, "\n")
# print(df2.describe(), "\n")
# print(df2.T, "\n")
# print(df2.sort_values(by='age'), "\n")

## Slicing DataFrame
# print("Sling DataFrame: \n")
# print(df2[1:4], "\n")
# print(df2.sort_values(by='age')[1:3], "\n")

# print("Query DataFrame by tag: \n")
# print(df2[['age', 'visits']], "\n")
# df3 = df2.copy()
# print(df3, "\n")
# print(df3.isnull(), "\n")
# df3.loc['f', 'age'] = 1.5
# print(df3, "\n")
# print(df3[['age']].mean(), "\n")
# print("Max: ", df3['visits'].max(), "\n")
# print("Min: ", df3['visits'].min(), "\n")
# print("Sum: ", df3['visits'].sum(), "\n")
# print("Sum: ", df3['visits'].sum(), "\n")
# print("Sum: \n", df3.sum(), "\n")
# print("Mean: \n", df3.mean(), "\n")
# print(pd.Series(['A', 'C', 'D', 'Aaa', 'BaCa', np.nan, 'CBA', 'Cow', 'Owl']))

## Operations for DataFrame missing values

# df4  = df3.copy()
# meanAge = df4['age'].mean()
# df4['age'].fillna(meanAge)
# print(df4['age'], "\n")

# df5 = df3.copy()
# print(df5.dropna(how='any'))


# File - related operations on dataframe #

# print(df3.to_csv('animal.csv'), "\n")

# df_animal = pd.read_csv('animal.csv')
# print(df_animal, "\n")

# print(df_animal.head(3), "\n")

# print(df3.to_excel('animal.xlsx', sheet_name='Sheet1'))

# df_animal2 = pd.read_excel('animal.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
# print(df_animal2)


# Visualization #


# Practice Exxaxmple #