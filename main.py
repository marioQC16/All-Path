# Importing needed libraries
import os.path
from math import sqrt
import numpy as np
import pandas as pd
#  import matplotlib

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

# method used to print arrays
def printArray(array, num):
    for i in range(num):
        print(array[i])

# method call for line count.
lineNum = simpleCount(fileName)

# getting size of matrices
num = int(sqrt(lineNum))

# adding the identity matrix
# and the adjacency matrix
# returns the not visited matrix
def addMatrices(array1, array2):
    tempArray = array1.__add__(array2)
    return np.logical_not(tempArray).astype(int)

# prints the components of a list
def printSlices(list, num, k):
    for i in range(num):
        print(f"{k}{i + 1} is {list[i]}")

# creating empty list to create matrix
list1 = []

# Converting data frame from 2-D to 1-D list
for i in range(lineNum):
    list1.append(df[1][i])

# Converting 1-D list to 1-D dataframe
df1 = pd.DataFrame({"A": list1})

# Converting dataframe into an adjacency matrix
adjMatrix = df1.values.reshape(num, num)

# Printing adjacency matrix
print("Our adjacency matrix is:")
printArray(adjMatrix,num)

# Slicing adjacency matrix
# into n number of slices
adjMatrixList = adjMatrix.tolist()
print("\nOur slices are:")
printSlices(adjMatrixList,num, "s" )
# Getting individual slices to print.

# getting identity matrix as int
idMatrix = np.identity(num, dtype=int)
print("\nThe identity matrix:")
printArray(idMatrix, num)

# getting not visited array
nvArray = addMatrices(adjMatrix, idMatrix)
print("\nThe not visited array")
printArray(nvArray, num)

# Slicing not visited matrix
# into n number of slices
nvArrList = nvArray.tolist()
print("\nOur not visited slices are:")
printSlices(nvArrList, num, "n")

# method used to create list of visited nodes
# it takes two list
# the first list is the adjMatrix list
# the second list is the indexList
# and in addition it takes the count variable
def makeList(l, m, count):
    for inner_l in l:
        for item in inner_l:
            count += 1
            if item == 1:
                m.append(count)
    return m.append(count)

# empty index list used keep track of visited nodes
indexList = []

# Counter for indices
count = 0

# function call to makeList method
makeList(adjMatrixList, indexList, count)

# updating count
count = indexList[-1]

# removing the result of count from indexList
del indexList[-1]

print("\n Our indices are: \n",indexList)
print(f"count is {count}")