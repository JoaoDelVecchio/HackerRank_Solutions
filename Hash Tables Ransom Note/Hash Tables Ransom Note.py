#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    mapa = {}
    for word in magazine:
        if word not in mapa:
            mapa[word] = 1
        else:
            mapa[word] += 1
    for word in note:
        if word not in mapa:
            print("No")
            return
        else:
            if mapa[word] == 0:
                print("No")
                return
            else:
                mapa[word] -= 1
                
    print("Yes")
            
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
