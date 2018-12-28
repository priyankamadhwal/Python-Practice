from itertools import combinations_with_replacement
string, K = input().split()
string, K = sorted(list(string)), int(K)
print('\n'.join([''.join(x) for x in combinations_with_replacement(string,K)]))
