n, arr = int(input()), list(map(int, input().split()))
pos, neg, zero = 0,0,0
for x in arr:
    if x > 0 : pos += 1
    elif x == 0 : zero += 1
    else : neg += 1
print('{0:.6f}\n{1:.6f}\n{2:.6f}'.format(pos/n,neg/n,zero/n))
