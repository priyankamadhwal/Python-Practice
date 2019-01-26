n, candles = int(input()), list(map(int,input().split()))
candles.sort(reverse=True)
print(candles.count(candles[0]))
