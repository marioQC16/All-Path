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

# getting size of matrices
num = int(sqrt(lineNum))


# getting match indices to iterate
# to iterate through next level of
# allPath array
def iterateList(nv, edge, num, idNum):
    if idNum % num == 0:
        nv = idNum // num
        while nv >= num:
            nv = nv // num
        nv -= 1
        edge = num - 1
    else:
        nv = idNum // num
        while nv > num:
            nv = nv // num
        if idNum > num ** 2:
            nv -= 1
        edge = idNum % num - 1

    return nv, edge


# Using logical to get next slice for AllPath
def getAnd(l1, l2):
    return np.logical_and(l1, l2).astype(int)


# Using logical or to get next slice for AllPath
def getOR(l1, l2):
    return np.logical_or(l1, l2).astype(int)


# get the number of nodes nv for each
# slice in level of array
def getSumSlice(l, s):
    temp = []
    for i in range(s, len(l)):
        n = sum(l[i])
        temp.append(n)
    return temp


list1 = []
# Converting dataframe into an adjacency matrix
adjMatrix = getAdjMatrix(df, list1, lineNum, num)

# Slicing adjacency matrix
# into n number of slices
adjMatrixList = adjMatrix.tolist()

# getting identity matrix as int
idMatrix = np.identity(num, dtype=int)

# getting not visited array
nvArray = getNVMatrix(adjMatrix, idMatrix)

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

# function calls
countNv = []
countSl = []
countNv = getSumSlice(nvArrList, 0)
countSl = getSumSlice(adjMatrixList, 0)
print("our nv count is ", countNv)
print("our sl count is ", countSl)

# Empty list for new slices
getSlice = []

#PROBLEM HERE for some reason it isn't adding the last one i need it to
# Method updates index list
def updateIndList(n, l, count):
    #print("start")
    for i in range(len(n)):
        #print(n[i])
        if n[i] == 0:
            count += 1
        else:
            count += 1
            l.append(count)
    #print("end")


# Gets next Level of the NV List
def getLevelNV(numVL, getSlice, nvArrList, countNv):
    while len(getSlice) != 0:
        if len(getSlice) >= 2:
            temp = getSlice.pop(0)
            temp1 = getSlice.pop(0)
            newList = getOR(temp, temp1).tolist()
            getSlice.append(newList)
        else:
            temp = getSlice.pop(0)
            temp = np.logical_not(temp)
            newNVSlice = getAnd(nvArrList[numVL], temp).tolist()
            countNv[numVL] = sum(newNVSlice)
            nvArrList[numVL] = newNVSlice


# Allows for exit of while loop
exSum = sum(countNv)

# Allows for adding a list of n-length
# to be added to adjMatrixList
addIndex = 0
nList = [0] * num

# Iterator used for nvArrList
numVL = 0

# Iterator use for iterating through adjMatrix
idCount = 0

# Performs next level operations for AllPath algorthim
while exSum != 0:
    if addIndex != indexList[idCount] - 1:
        # adds empty list to adjMatrixList
        adjMatrixList.append(nList)
        # adds length of list to count
        count += len(nList)
    else:
        # combines n and s slices
        temp = []
        temp = iterateList(nvArrList, adjMatrixList, num, indexList[idCount])
        print(temp)
        nv = nvArrList[temp[0]]
        print(indexList[idCount])
        print(f"not visited {nv}")
        edge = adjMatrixList[temp[1]]
        print(f"edges {edge}")
        nVe = getAnd(nv, edge)
        print(f"New NV{nVe}")
        nVe = nVe.tolist()
        if sum(nVe) == 0:
            # updating count for empty slices
            count += len(nList)
        else:
            # updating count for non-empty slices
            updateIndList(nVe, indexList, count)
            count += len(nList)
        # getSlice used for next level nv
        getSlice.append(nVe)
        # appending adjMatrix
        adjMatrixList.append(nVe)
        #  updating iterator for index list
        idCount += 1
    # getting next level nv
    if len(getSlice) == countSl[numVL]:
        # call getLevel function to update various list
        getLevelNV(numVL, getSlice, nvArrList, countNv)
        # updating exit variable
        exSum = sum(countNv)
        # updating iterator for countNV and nvArrList
        if numVL < len(countNv) - 1:
            numVL += 1
    # updating iterator for 1st if statement
    addIndex += 1

# print(f"\nour exit sum is {exit sum}")

print(f"\nour new adj matrix list is\n {adjMatrixList}")
print(f"\nour new nv List is of {nvArrList}")
print(f"\nour index list is {indexList}")

"""
Write new code below this block


"""