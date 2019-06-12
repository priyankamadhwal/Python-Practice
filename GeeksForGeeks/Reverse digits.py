'''
Write a program to reverse digits of a number N.
'''

for _ in range(int(input())):
    N = int(input())
    nonZero = False
    rev = ''
    while N > 0:
        rem = N%10
        if rem!=0:
            nonZero = True
        if nonZero:
            rev += str(rem)
        N //= 10
    print(rev)
