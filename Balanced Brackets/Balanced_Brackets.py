#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
        
def isBalanced(s):
    # Write your code here
    pilha = Stack()
    achou = 0
    for elem in s:
        if elem == '{' or elem == '[' or elem == '(':
            pilha.push(elem)
        else:
            if pilha.is_empty():
                achou = 1
                break
            else:
                if elem == ')' and pilha.top() == '(':
                    pilha.pop()
                elif elem == ']' and pilha.top() == '[':
                    pilha.pop()
                elif elem == '}' and pilha.top() == '{':
                    pilha.pop()
                else:
                    achou = 1
                    break
                    
    if not pilha.is_empty():
        achou = 1
    if achou == 1:
        return "NO"
    else:
        return "YES"

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
