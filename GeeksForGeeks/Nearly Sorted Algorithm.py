'''
Given an array of n elements, where each element is at most k away from its target position. The task is to print array in sorted form.
'''

from heapq import heappush, heappop, heapify

for _ in range(int(input())):
    N, K = map(int,input().split())
    numbers = list(map(int,input().split()))
    sorted_N = []
    heap = numbers[:K+1] 
    heapify(heap)
    for rem in range(K+1,N):
        sorted_N.append(heappop(heap))
        heappush(heap,numbers[rem])
    while heap:
        sorted_N.append(heappop(heap))
    for i in sorted_N:
        print(i,end=" ")
    print()
