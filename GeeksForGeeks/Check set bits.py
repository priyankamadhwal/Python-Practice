'''
Given a number N. Write a program to check whether every bit in the binary representation of the given number is set or not.
'''

for _ in range(int(input())):
    number = int(input())
    isEveryBitSet = not ('0' in bin(number)[2:])
    print("YES" if isEveryBitSet else "NO")
