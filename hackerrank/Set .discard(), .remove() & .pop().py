n = int(input())
s = set(map(int, input().split()))
noCmd = int(input())
for _ in range(noCmd):
    cmd = input().split()
    if cmd[0] == 'pop':
        eval('s.pop()')
    else:
        eval('s.'+cmd[0]+'('+cmd[1]+')')
print(sum(s))
