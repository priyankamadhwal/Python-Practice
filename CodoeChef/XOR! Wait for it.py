# https://www.codechef.com/problems/XORNEY

'''
If the count of Odd Numbers is even, Final XOR = Even
If the count of Odd Numbers is Odd, Final XOR = Odd
'''

for _ in range(int(input())):
    L, R = map(int,input().split())
    oddCount = (R - L) // 2
    if R % 2 == 1 or L % 2 == 1: oddCount += 1 
    print ('Even' if oddCount % 2 == 0 else 'Odd') 
