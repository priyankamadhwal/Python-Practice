from collections import OrderedDict
words = OrderedDict()
N = int(input())
for _ in range(N):
    curr = input()
    if curr in words: words[curr] += 1
    else: words[curr] = 1
print(len(words),' '.join(map(str,[words[x] for x in words])), sep='\n')
