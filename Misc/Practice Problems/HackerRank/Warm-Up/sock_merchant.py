#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #n = number of socks
    #ar = list of socks in any order
    """
    METHOD 1 - BRUTE FORCE
    ar.sort()
    counter = 0
    check = False
    for i in range(len(ar)-1):
        if check == True:
            check = False
            continue
        first_num = ar[i]
        for j in range(i+1, len(ar)):
            second_num = ar[j]
            if first_num == second_num and check == False:
                counter += 1
                check = True
    return counter
    """

    """
    METHOD 2 - Using sets
    """
    s = set()
    count = 0
    for color in ar:
        if color in s:
            s.remove(color)
            count += 1
        else:
            s.add(color)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()