'''
Given a positive integer N, print count of set bits in it. 
For example, if the given number is 6(binary: 110), output should be 2 as there are two set bits in it.
'''

for _ in range(int(input())):
    print(bin(int(input())).count('1'))
