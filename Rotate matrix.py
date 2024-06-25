from math import *
from collections import *
from sys import *
from os import *

def rotateMatrix(mat, n, m):
    l, r, b, t = 0, m - 1, n - 1, 0
    while (l < r and t < b):
        mat = clockwise(mat, l, r, b, t)
        l += 1
        r -= 1
        t += 1
        b -= 1
    return mat

def clockwise(mat, l, r, b, t):
    temp = mat[t][l]
    #Left to right
    for i in range(l, r):
        temp, mat[t][i + 1] = mat[t][i + 1], temp
    #Top to bottom
    for i in range(t, b):
        temp, mat[i + 1][r] = mat[i + 1][r], temp
    #right to left
    for i in range(r, l, -1):
        temp, mat[b][i - 1] = mat[b][i - 1], temp
    #bottom to top
    for i in range(b, t, -1):
        temp, mat[i - 1][l] = mat[i - 1][l], temp
    return mat
    
