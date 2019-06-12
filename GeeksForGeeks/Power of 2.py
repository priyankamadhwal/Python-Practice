'''
Given a positive integer N. The task is to check if N is a power of 2. That is N is 2^x for some x.
'''

import math
for _ in range(int(input())):
    N = int(input())
    B = bin(N)
    print('YES' if B.count('1')==1 else 'NO')
