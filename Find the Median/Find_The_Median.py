#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    v = sorted(arr)
        
    n = len(arr)
    if (n%2 != 0):
        k = int(n/2)
        return (v[k])
    else:
        k = int(n/2)
        j = int(n/2 - 1)
        return (v[k]+v[j])/2
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
