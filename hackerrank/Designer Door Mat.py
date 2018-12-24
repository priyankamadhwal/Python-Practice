if __name__ == '__main__':
    N,M = map(int,input().split())
    for i in range(1,N//2+1):
        pattern = '.|.'*(2*i-1)
        pattern = pattern.center(M,'-')
        print(pattern)
    print('WELCOME'.center(M,'-'))
    for i in range(N//2,0,-1):
        pattern = '.|.'*(2*i-1)
        pattern = pattern.center(M,'-')
        print(pattern)
