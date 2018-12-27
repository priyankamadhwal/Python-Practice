if __name__ == '__main__':
    n, m = map(int,input().split())
    array, A, B = list(map(int,input().split())), set(map(int,input().split())), set(map(int, input().split()))
    happiness = 0
    happiness = sum ([(e in A) -(e in B) for e in array])
    print(happiness)
