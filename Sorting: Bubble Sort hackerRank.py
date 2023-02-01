#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n=a
    s=0
    unsortedIndex=len(n)-1
    for j in range(0,unsortedIndex):
        for i in range(0, unsortedIndex):
            if n[i] > n[i + 1]:
                s=s+1
                temp=n[i]
                n[i]= n[i + 1]
                n[i+1]=temp
        unsortedIndex=unsortedIndex-1
    return print('Array is sorted in',s,'swaps.'),print('First Element:',n[0]),print(f'Last Element: {n[len(n)-1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)


# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
