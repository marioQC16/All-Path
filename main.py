# Importing needed libraries
import os.path
from math import sqrt
import numpy as np
import pandas as pd

# changing filepath to a variable name
fileName = "./testAlgorithm.csv"

# opening file, doing file check, converting
# file to dataframe
if os.path.isfile(fileName):
    with open(fileName, "r"):
        df = pd.read_csv(fileName, header=None)
else:
    print(f"file{fileName} does not exist")

# method used to count the number of lines
# in data file
def simpleCount(fileName):
    lines = 0
    for line in open(fileName):
        lines += 1
    return lines

# method call for line count.
lineNum = simpleCount(fileName)

# getting denominator
num = int(sqrt(lineNum))

# creating empty list to create matrix
list1 =[]

# Converting data frame from 2-D to 1-D list
for i in range(lineNum):
    list1.append(df[1][i])

# Converting 1-D list to 1-D dataframe
df1 = pd.DataFrame({"A":list1})

# Converting dataframe into an adjacency matrix
adjMatrix = df1.values.reshape(num, num)

# Printing adjacency matrix
print(f"Our adjacency matrix is: \n {adjMatrix}\n")

# Slicing adjacency matrix
# into n number of slices
adjMatrixList = adjMatrix.tolist()

print("Our slices are:")

# Getting individual slices to print.
for i in range(num):
    print(f"s{i + 1} is {adjMatrixList[i]}")


