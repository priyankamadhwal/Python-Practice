T = int(input())
for _ in range(T):
    N, A, M, B = int(input()), set(map(int,input().split())), int(input()), set(map(int,input().split()))
    print (A.intersection(B) == A)
