'''
In operating systems that use paging for memory management, page replacement algorithm are needed to decide which page needs to be 
replaced when the new page comes in. 
Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the existing 
pages with a newly needed page. 
Given a sequence of pages and memory capacity, your task is to find the number of page faults using Least Recently Used (LRU) Algorithm.
'''

for _ in range(int(input())):
    n = int(input())
    pages = list(map(int,input().split()))
    memoryCapacity = int(input())
    pageFaults = 0
    inMemory = []
    for x in pages:
        if x not in inMemory:
            pageFaults += 1 
            if inMemory and len(inMemory)==memoryCapacity:
                inMemory.pop(0)
        else:
            inMemory.pop(inMemory.index(x))
        inMemory.append(x)
    print(pageFaults)
