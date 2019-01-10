# https://www.hackerearth.com/problem/algorithm/picking-the-coins-50470dca/

for _ in range(int(input())):
    N, k = map(int,input().split())
    alice = True    # Alice's turn first
    pick, i = 0, 1
    if k == 1:
        print('Alice' if N%2 is 1 else 'Bob')
    else:
        while True:
            pick = k**i
            # Alice
            if pick > N : 
                alice = False
                break
            N -= pick
            # Bob
            if pick > N : 
                break
            N -= pick
            i += 1
        print('Alice' if alice else 'Bob')
