'''
Given a number N and a value K. From the right, set the Kth bit in the binary representation of N. 
The position of LSB(or last bit) is 0, second last bit is 1 and so on. 
Also, 0 <= K < X, where X is the number of bits in the binary representation of N.
'''

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    B = bin(N)
    B = B[::-1]
    B = (B[:K]+'1'+B[K+1:])[::-1]
    print(int(B,2))
