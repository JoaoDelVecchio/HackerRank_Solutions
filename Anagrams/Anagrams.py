#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    mapa = {}
    pairs = 0
    for i in range(1, len(s)+1):    # i representa o tamanho da substring
        for j in range(len(s) - i + 1):
            x = ''.join(sorted(s[j:j+i]))
            print(x)
            if x not in mapa:
                mapa[x] = 1
            else:
                pairs += mapa[x]
                mapa[x] += 1
    return pairs
            
                
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()