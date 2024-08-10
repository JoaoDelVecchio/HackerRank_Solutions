#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    vetor = [0]*(n+1)
    maximo = 0
    
    for query in queries:
        inicio = query[0] - 1
        fim = query[1]
        incremento = query[2]
        vetor[inicio] += incremento
        vetor[fim] -= incremento
    soma_atual = 0
    
    for i in range(n):
        soma_atual += vetor[i]
        if soma_atual > maximo:
            maximo = soma_atual
    return maximo
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
