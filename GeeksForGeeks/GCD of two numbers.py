'''
Given two numbers A and B. The task is to find the GCD of those 2 numbers.
'''

import math
for _ in range(int(input())):
    A, B = map(int,input().split())
    print(math.gcd(A,B))
