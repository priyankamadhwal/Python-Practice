from collections import deque
T = int(input())
for _ in range(T):
    N, cubes, pile, flag = int(input()), deque(map(int,input().split())), [], True
    while len(cubes) > 0 and flag:
        left, right = cubes[0], cubes[len(cubes)-1]
        if pile == []:
            if left >= right : pile.append(cubes.popleft())
            else: pile.append(cubes.pop())
        else:
            if left >= right and left <= pile[len(pile)-1]: pile.append(cubes.popleft())
            elif right <= pile[len(pile)-1]: pile.append(cubes.pop())
            else: flag = False
    if flag: print('Yes')
    else: print('No')
