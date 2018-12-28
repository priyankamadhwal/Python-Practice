from collections import Counter
X, shoeSizes, N = int(input()), Counter(map(int,input().split())), int(input())
moneyEarned = 0
for _ in range(N):
    size, price = map(int,input().split())
    if shoeSizes[size]: 
        moneyEarned += price
        shoeSizes[size] -= 1
print(moneyEarned)
