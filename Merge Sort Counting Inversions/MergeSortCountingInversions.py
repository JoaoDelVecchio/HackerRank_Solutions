#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def mergeSort(ini, fim, arr):
    count = 0
    if fim - ini == 1:
        if arr[fim] < arr[ini]:
            arr[fim], arr[ini] = arr[ini], arr[fim]
            count += 1
    if fim - ini > 1:
        mid = int((fim + ini) / 2)
        count += mergeSort(ini, mid, arr)
        count += mergeSort(mid+1, fim, arr)
        count += merge(ini, mid, fim, arr)
    return count
    pass

def merge(ini, mid, fim, arr):
    count = 0
    aux = []
    i, j = ini, mid + 1
    
    while j<=fim and i <= mid:
        aux.append(min(arr[i], arr[j]))
        if arr[i] <= arr[j]:
            i += 1
        else:
            j+=1
            count += mid - i + 1
    
    if j > fim:
        while i <= mid:
            aux.append(arr[i])
            i += 1
    if i > mid:
        while j <= fim:
            aux.append(arr[j])
            j += 1
    
    for k in range(len(aux)):
        arr[ini + k] = aux[k]
    return count
    pass

def countInversions(arr):
    swaps = mergeSort(0, len(arr)-1, arr)
    return swaps
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
