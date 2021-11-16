# Importing needed libraries
import os.path
from math import sqrt
import numpy as np
import pandas as pd
import requests
import sys
import glob


def initialSetup(graphFile):
    # changing filepath to a variable name
    global fileName
    fileName = graphFile

    # opening file, doing file check, converting
    # file to dataframe
    global df
    if os.path.isfile(fileName):
        with open(fileName, "r"):
            df = pd.read_csv(fileName, header=None)
    else:
        print(f"file{fileName} does not exist")

    # method call for line count.
    global lineNum
    lineNum = simpleCount(fileName)

    # getting size of matrices
    global num
    num = int(sqrt(lineNum))


# method used to count the number of lines
# in data file
def simpleCount(fileName):
    lines = 0
    for line in open(fileName):
        lines += 1
    return lines


# empty index list used keep track of visited nodes
indexList = []


# Level Checker
def checkLevel(indexNumber, nodes):
    level = 0
    while indexNumber > nodes:
        indexNumber = indexNumber // nodes
        level += 1
    return level


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


def levelSummation(level, nodes):
    sum = 0
    while level > 1:
        sum += (nodes ** level)
        level -= 1
    return sum


# getting match indices to iterate
# to iterate through next level of
# allPath array
def iterateList(nv, edge, num, idNum):
    level = checkLevel(idNum, num)
    if level == 0:
        level = 1
    levelSum = levelSummation(level, num)
    if idNum % num == 0:
        if level == 1:
            nv = ((idNum - levelSum) // (num ** level)) - 1
        else:
            nv = ((idNum - levelSum) // (num ** level))
        edge = num - 1
    else:
        nv = (idNum - levelSum) // (num ** level)
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


# Method updates index list
def updateIndList(n, l, count):
    # print("start")
    for i in range(len(n)):
        # print(n[i])
        if n[i] == 0:
            count += 1
        else:
            count += 1
            l.append(count)
    # print("end")


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
            if sum(newNVSlice) < countNv[numVL]:
                countNv[numVL] = sum(newNVSlice)
            nvArrList[numVL] = newNVSlice

# Finds the nodes in between start and end
def findMiddleNodes(nodes, currentLevel, indexNumber):
    middleString = ""
    middleNumber = 0
    while currentLevel > 1:
        middleNumber = int(((indexNumber % (nodes ** currentLevel)) / (nodes ** (currentLevel - 1))) + 1)
        middleString += str(middleNumber)
        middleString += ", "
        currentLevel -= 1
    return middleString




# Finds the shortest path from one node to another
def shortestPath(index, nodes, start, end):
    if(end < 1 or end > num):
        print("The Ending node is not in range of the graph")
    elif(start < 1 or start > num):
        print("The Starting node is not in range of the graph")
    else:
        for i in range(len(index)):
            level = checkLevel(index[i], nodes)
            if level == 0:
                level = 1
            levelSum = levelSummation(level, nodes)
            indexNumber = index[i] - levelSum
            mod = (indexNumber % nodes)
            if mod == 0:
                mod = nodes
            if int(mod) == int(end):
                if indexNumber % nodes == 0 and level == 1:
                    if int((indexNumber / (nodes ** level))) == int(start):
                        middle = findMiddleNodes(nodes, level, indexNumber)
                        print("The shortest path from", sys.argv[1], "to", sys.argv[2], "is " + str(start) + ", " + middle + str(end))
                else:
                    if int((indexNumber / (nodes ** level)) + 1) == int(start):
                        middle = findMiddleNodes(nodes, level, indexNumber)
                        print("The shortest path from", sys.argv[1], "to", sys.argv[2], "is " + str(start) + ", " + middle + str(end))




def indexGraph(graphName):
    initialSetup(graphName)

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
   

    # Empty list for new slices
    getSlice = []

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
            nv = nvArrList[temp[0]]
            edge = adjMatrixList[temp[1]]
            nVe = getAnd(nv, edge)
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
            oldNV = sum(countNv)
            getLevelNV(numVL, getSlice, nvArrList, countNv)

            # This condition is what they call a Spike Solution, it works for now but likely won't hold
            if (sum(countNv) == oldNV) and countNv[numVL] != 0 and sum(countNv) < num:
                countNv[numVL] -= 1
            # updating exit variable
            exSum = sum(countNv)
            # updating iterator for countNV and nvArrList

            if numVL < len(countNv):
                numVL += 1
                if numVL == len(countNv):
                    numVL = 0
                while countNv[numVL] == 0 and numVL < len(countNv) - 1:
                    numVL += 1

        # updating iterator for 1st if statement
        addIndex += 1
        # This works because it is ABSOLUTELY impossible for an index value to be greater than the Summation of
        # number of nodes to the number of nodes power, adding every exponent down to node^2
        if indexList[idCount] > levelSummation(num, num):
            exSum = 0

    
    return ""


"""
Write new code below this block


"""
newest = min(glob.iglob('./uploads/*.csv'), key=os.path.getctime)

print(indexGraph(newest))
startNode = int(sys.argv[1])

endNode = int(sys.argv[2])


shortestPath(indexList, num, startNode, endNode)
