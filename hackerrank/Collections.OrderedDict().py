from collections import OrderedDict
N = int(input())
allItems = OrderedDict()
for _ in range(N):
    curr = input().split()
    item, price = " ".join(curr[:len(curr)-1]), int(curr[len(curr)-1])
    if item in allItems : allItems[item] += price
    else: allItems[item] = price
for x in allItems:
    print(x,allItems[x])
