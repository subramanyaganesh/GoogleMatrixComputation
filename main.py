import math

import numpy as np

row = 10
column = 10
precisionDigit = 4

webTopology = np.zeros(shape=(row, column), dtype=int)
hyperlinkMatrix = np.zeros(shape=(row, column), dtype=float)
googleMatrix = np.zeros(shape=(row, column), dtype=float)
initialMatrix = np.zeros(shape=(row, column), dtype=float)
initialMatrix[:, :] = 1 / 10
v0 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# v0 = np.zeros(shape=(1, column), dtype=float)
# v1 = np.zeros(shape=(1, column), dtype=float)
# v0[:, :] = 1 / 10

a = [[2, 5, 6, 8], [2, 4, 6, 8], [0, 1, 6], [0, 2, 6, 8], [2, 8], [0, 3, 6], [0, 2, 8], [0, 2, 8], [6], [0, 2, 6, 8]]


def roundUp(f, n):
    return [round(p, n) for p in f]


def truncate(f, n):
    return [math.floor(p * 10 ** n) / 10 ** n for p in f]


rows = -1
for arrays in a:
    rows += 1
    for columns in arrays:
        webTopology[rows, columns] = 1
        hyperlinkMatrix[rows, columns] = webTopology[rows, columns] / len(arrays)
    continue


dampingFactor = 0.85
googleMatrix = dampingFactor * hyperlinkMatrix + (1 - dampingFactor) * initialMatrix

# print(googleMatrix)
count = 0
while True:
    count += 1
    v1 = v0 @ googleMatrix
    if (truncate(v0, precisionDigit) == truncate(v1, precisionDigit)):
        break
    v0 = v1
print(v0[5],v0[7])
print(count)

print(roundUp(v0, precisionDigit))
