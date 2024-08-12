#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    matrix = [[0 for j in range(len(s2))] for i in range(len(s1))]
    
    if s1[0] == s2[0]:
        matrix[0][0] = 1
    else:
        matrix[0][0] = 0
    for j in range(1, len(s2)):
        if s1[0] == s2[j]:
            matrix[0][j] = 1
        else:
            matrix[0][j] = matrix[0][j-1]
    for i in range(1, len(s1)):
        if s2[0] == s1[i]:
            matrix[i][0] = 1
        else:
            matrix[i][0] = matrix[i-1][0]
    
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    
    return matrix[len(s1)-1][len(s2)-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
