size, A, N = int(input()), set(map(int, input().split())), int(input())
for _ in range(N):
    op, length = input().split()
    givenSet = set(map(int, input().split()))
    eval('A.'+op+'(givenSet)')
print(sum(A))
