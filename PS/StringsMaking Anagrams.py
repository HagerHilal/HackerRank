#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # a is the first string 
    # b is the second string
    a_len = len(a) 
    b_len = len (b)
    intersection = ''
    for i in a:
        for j in b :
            if j == i :
                intersection += i
                a  = a.replace( i , '' , 1)
                b = b.replace( j , '', 1)
                break
    return (a_len - len(intersection ) ) + (b_len - len(intersection ))

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
