#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    # Em cada linha: transformar a string em lista, ordenar a lista, transformar a lista em string, substituir a string do grid por essa nova string
    # comparar o elemento i de cada string, variando da linha 0 ate o tamanho total. Se ocorrer algum elemento maior que o anterior, entao nao esta ordenado.
    lista = []
    for i, string in enumerate(grid):
        lista.append(list(string))
        lista[i].sort()
    
    m = len(lista[0])
    n = len(lista)
    
    for j in range(m):
        anterior = lista[0][j]
        for i in range(n):
            if (lista[i][j] < anterior):
                return "NO"
            anterior = lista[i][j]
    return "YES"
            
        
    
     
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
