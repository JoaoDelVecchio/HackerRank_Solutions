#!/bin/python3

import math
import os
import random
import re
import sys


def freqQuery(queries):
    freq_map = {}
    count_map = {}
    result = []
    count_map[1] = 0
    count_map[0] = 0
    for query in queries:
        op, value = query
        
        if op == 1:
            if value in freq_map:
                count_map[freq_map[value]] -= 1
                freq_map[value] += 1
                if freq_map[value] in count_map:
                    count_map[freq_map[value]] += 1
                else:
                    count_map[freq_map[value]] = 1
            else:
                freq_map[value] = 1
                count_map[1] += 1
                
        if op == 2:
            if value in freq_map:
                count_map[freq_map[value]] -= 1
                freq_map[value] -= 1
                count_map[freq_map[value]] += 1
                if freq_map[value] == 0:
                    del freq_map[value]
        
        if op == 3:
            if value in count_map and count_map[value] > 0:
                result.append(1)
            else:
                result.append(0)
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
