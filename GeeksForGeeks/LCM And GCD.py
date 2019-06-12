'''
Given two numbers A and B. The task is to find out their LCM and GCD.
'''

import math
def gcd(a,b):
    return math.gcd(a,b)

def lcm(a,b):
    return a*b//gcd(a,b)
    
for _ in range(int(input())):
    A, B = map(int,input().split())
    print(lcm(A,B),gcd(A,B))
