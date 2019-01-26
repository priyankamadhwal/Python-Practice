n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
diag1, diag2 = 0,0
for i in range(n):
    diag1 += a[i][i]
    diag2 += a[i][(n-1)-i]
print(abs(diag1-diag2))
