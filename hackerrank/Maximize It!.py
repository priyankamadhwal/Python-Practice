from itertools import product
K, M = map(int, input().split()) 
elements = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*elements))
print(max(results))
