a, b = list(map(int,input().split())), list(map(int,input().split()))
alice, bob = 0,0
for i, j in zip(a,b):
    if i > j : alice += 1
    elif j > i : bob += 1
print(alice, bob)
