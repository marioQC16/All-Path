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
# use as numerator
lineNum = simpleCount(fileName)

# getting denominator
num = int(sqrt(lineNum))

list1 =[]

for i in range(lineNum):
    list1.append(df[1][i])

df1 = pd.DataFrame({"A":list1})
adjMatrix = df1.values.reshape(num, num)
print(adjMatrix)
adjMatrixList = adjMatrix.tolist()
s1 = adjMatrixList[0]

print(s1)  