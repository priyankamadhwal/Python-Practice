from collections import deque
d = deque()
for _ in range(int(input())):
    cmd = input().split()
    if len(cmd) == 1: eval('d.'+cmd[0]+'()')
    else: eval('d.'+cmd[0]+'('+cmd[1]+')')
print(' '.join(map(str,[x for x in d])))
