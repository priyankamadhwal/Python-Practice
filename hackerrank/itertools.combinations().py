from itertools import combinations
string, K = input().split()
string, K = sorted(list(string)), int(K)
for i in range(1,K+1):
    print('\n'.join([''.join(x) for x in combinations(string,i)]))
