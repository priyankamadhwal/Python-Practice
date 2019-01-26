n = int(input())
for i in range(1,n+1):
    current = '#'*i
    print(current.rjust(n,' '))
