'''
Given an array consisting cost of toys. 
Given an integer K depicting the amount with you. 
Maximise the number of toys you can have with K amount.
'''

for _ in range(int(input())):
    N, K = map(int,input().split())
    toys_cost = sorted(list(map(int,input().split())))
    currCost, totalToys = 0, 0
    for x in toys_cost:
        if currCost+x <= K:
            currCost = currCost+x
            totalToys += 1
        else:
            break
    print(totalToys)
