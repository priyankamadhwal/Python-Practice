from itertools import permutations
string, K = input().split()
K = int(K)
string = sorted(list(string))
print('\n'.join([''.join(x) for x in list(permutations(string,K))]))
