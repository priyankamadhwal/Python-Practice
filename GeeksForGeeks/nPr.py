'''
Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.
'''

import math
for _ in range(int(input())):
    n, r = map(int, input().split())
    print(int(math.factorial(n)/math.factorial(n-r)))
