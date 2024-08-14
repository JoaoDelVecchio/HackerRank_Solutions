#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    vet = [float('inf')]*len(p)
    ind = [-1]*len(p)
    aux = 0
    dias = 0
    for i in range(1, len(p)):
        j = i - 1
        Achou = False
        aux = 0
        while not Achou:
            if p[j] >= p[i]:
                if vet[j] == float('inf'):
                    Achou = True
                else:
                    aux = vet[j]
                    j = ind[j]
            else:
                if vet[j] > aux:
                    vet[i] = aux + 1
                    dias = max(dias, vet[i])
                    ind[i] = j
                    Achou = True
                else:
                    j = ind[j]
    return dias
                    
                
                
                    
        
            
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()