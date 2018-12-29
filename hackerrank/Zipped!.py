N, X = map(int,input().split())
marks = [list(map(float,input().split())) for _ in range(X)]
print(*[sum(list(x))/X for x in list(zip (*marks))],sep='\n')
