#!/bin/python3

import math
import os
import random
import re
import sys

def countTriplets(arr, r):
    count = {}
    triplet_count = {}
    triplets = 0

    for val in arr:
        if val in triplet_count:
            triplets += triplet_count[val]
        
        if val in count:
            if val * r not in triplet_count:
                triplet_count[val * r] = 0
            triplet_count[val * r] += count[val]

        if val * r not in count:
            count[val * r] = 0
        count[val * r] += 1

    return triplets
            
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
