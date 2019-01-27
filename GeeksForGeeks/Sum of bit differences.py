for _ in range(int(input())):
    n, array = int(input()), list(map(int, input().split()))
    pairsXor, sumBitDiff = [x^y for x in array for y in array], 0
    for curr in pairsXor:
        sumBitDiff += bin(curr).count('1')
    print(sumBitDiff)
