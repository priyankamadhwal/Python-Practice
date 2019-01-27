# https://www.codechef.com/problems/WTCH

for _ in range(int(input())):
    N, S, maxCount = int(input()), input(), 0
    if N == 1:
        if S[0]=='0': print(1)
        else: print(0)
    else:
        if S[0] == '0' and S[1] == '0':
            S = '1'+S[1:]
            maxCount += 1
        for i in range(1,N-1):
            if S[i] == '0' and S[i-1] == '0' and S[i+1] == '0':
                    S = S[:i]+'1'+S[i+1:]
                    maxCount += 1
        if S[N-2]=='0' and S[N-1]=='0':
            maxCount += 1
        print(maxCount)
