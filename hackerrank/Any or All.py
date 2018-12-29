N, num = int(input()), list(map(int,input().split()))
print(all([i>0 for i in num]) and any([j==int(str(j)[::-1]) for j in num]))
