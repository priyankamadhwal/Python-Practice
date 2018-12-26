#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    name = s.split(' ')
    for i in range(len(name)):
        if name[i] != '' and name[i][0].isalpha():
            name[i] = name[i].title()
    return " ".join(name)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    
    fptr.write(result + '\n')

    fptr.close()
