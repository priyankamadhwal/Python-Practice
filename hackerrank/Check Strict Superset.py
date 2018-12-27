A, n = set(map(int,input().split())), int(input())
B = [set(map(int,input().split())) for _ in range(n)]
print(all([A.intersection(X) == X and A != X for X in B]))
