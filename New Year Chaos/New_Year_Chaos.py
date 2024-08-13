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
def tooChaotic(q):
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            return True
    return False
def minimumBribes(q):
    count = 0
    if tooChaotic(q):
        print("Too chaotic")
        return
    else:
        for i in range(len(q) - 1, -1, -1):
            if q[i] != i + 1:
                if q[i-1] == i+1:
                    q[i-1], q[i] = q[i], q[i-1]
                    count += 1
                if q[i-2] == i+1:
                    q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
                    count += 2
        print(count)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
