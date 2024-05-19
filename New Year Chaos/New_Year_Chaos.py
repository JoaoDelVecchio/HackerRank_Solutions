#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    n = len(q)
    bribles = 0
    for i in range(n, 1, -1):
        if (q[i-1] != i):
            if i==2:
                if (q[i-2] == i):
                    aux = q[i-1]
                    q[i-1] = q[i-2]
                    q[i-2] = aux
                    bribles += 1
                    break
            if (q[i-2] == i):
                aux = q[i-1]
                q[i-1] = q[i-2]
                q[i-2] = aux
                bribles += 1
            else:
                if (q[i-3] == i):
                    aux = q[i-1]
                    q[i-1] = q[i-3]
                    q[i-3] = q[i-2]
                    q[i-2] = aux
                    bribles += 2
                else:
                    print("Too chaotic")
                    return
    print(bribles)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
