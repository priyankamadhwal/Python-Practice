'''
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.
'''

for _ in range(int(input())):
    N, S = map(int,input().split())
    result = None
    if (S > 9*N) or (S==0 and N>1):
        result = -1
    else:
        result = [0]*N
        for i in range(N):
            if S >= 9:
                result[i] = 9
                S -= 9
            else:
                result[i] = S
                break
        result = [str(x) for x in result]
        result = int(''.join(result))
    print(result)
