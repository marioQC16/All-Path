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


# Method used to create original index list
def getIndexList(df, indexList, count):
    for i in range(lineNum):
        count += 1
        if df[1][i] == 1:
            indexList.append(count)

    return indexList.append(count)


# Using the logical or operator
# on the identity matrix
# and the adjacency matrix
# returns the not visited matrix
def getNVMatrix(array1, array2):
    tempArray = array1.__or__(array2)
    return np.logical_not(tempArray).astype(int)


# prints the components of a list
def printSlices(list, num, k):
    for i in range(num):
        print(f"{k}{i + 1} is {list[i]}")


# Creating adjMatrix from a 2-d df
def getAdjMatrix(df, l, lineNum, num):
    for i in range(lineNum):
        l.append(df[1][i])
    df1 = pd.DataFrame({"A": l})
    return df1.values.reshape(num, num)


# method call for line count.
lineNum = simpleCount(fileName)
print(len(df))
# getting size of matrices
num = int(sqrt(lineNum))

list1 = []
# Converting dataframe into an adjacency matrix
adjMatrix = getAdjMatrix(df, list1, lineNum, num)

# Printing adjacency matrix
print("Our adjacency matrix is:")
printArray(adjMatrix, num)

# Slicing adjacency matrix
# into n number of slices
adjMatrixList = adjMatrix.tolist()
print("\nOur slices are:")
printSlices(adjMatrixList, num, "s")
# Getting individual slices to print.

# getting identity matrix as int
idMatrix = np.identity(num, dtype=int)
print("\nThe identity matrix:")
printArray(idMatrix, num)

# getting not visited array
nvArray = getNVMatrix(adjMatrix, idMatrix)
print("\nThe not visited array")
printArray(nvArray, num)

# empty index list used keep track of visited nodes
indexList = []

# Counter for indices
count = 0

id = getIndexList(df, indexList, count)
# updating count
count = indexList[-1]

# removing the result of count from indexList
del indexList[-1]

# Slicing not visited matrix
# into n number of slices
nvArrList = nvArray.tolist()
print("\nOur not visited slices are:")
printSlices(nvArrList, num, "n")

print(f"\nour index list is {indexList}")

print(f"\nour adj matrix list is\n {adjMatrixList}")

print(f"\nour nv matrix list is\n {nvArrList}")

# getting match indices to iterate
# to iterate through next level of
# allPath array
def iterateList (nv, edge, num, idNum):
    if idNum % num == 0:
        nv = idNum // num - 1
        edge = num - 1
    else:
        nv = idNum // num
        edge = idNum % num - 1

    return  nv, edge

# Using logical to get next slice for AllPath
def getAnd (l1, l2):
    return np.logical_and(l1,l2).astype(int)

# Using logical or to get next slice for AllPath
def getOR (l1, l2):
    return np.logical_or(l1, l2).astype(int)

# get the number of nodes nv for each
# slice in level of array
def getSumSlice(l, s):
    temp = []
    for i in range(s, len(l)):
        n = sum(l[i])
        temp.append(n)
    return temp

# function calls
countNv = []
countSl = []
countNv = getSumSlice(nvArrList, 0)
countSl = getSumSlice(adjMatrixList, 0)
print("our nv count is ",countNv)
print("our sl count is ",countSl)

# Empty list for new slices
getSlice = []

idCount = 0
nList = [0, 0, 0, 0]
for i in range(0, 16):
    if i != indexList[idCount]:
        adjMatrixList.append(nList)
    else:
        temp = []
        temp = iterateList(nvArrList, adjMatrixList, num, indexList[idCount])
        nv = nvArrList[temp[0]]
        edge = adjMatrixList[temp[1]]
        nVe = getAnd(nv, edge)
        nVe = nVe.tolist()
        getSlice.append(nVe)
        adjMatrixList.append(nVe)
        idCount += 1

print(f"\nour new adj matrix list is\n {adjMatrixList}")
print(f"our adjMatrix List is of {len(adjMatrixList)}")