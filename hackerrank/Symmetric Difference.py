if __name__ == '__main__':
    M, setA, N, setB = int(input()), set(map(int, input().split())), int(input()), set(map(int,input().split()))
    symDiff = list(setA.difference(setB).union(setB.difference(setA)))
    symDiff.sort()
    for x in symDiff:
        print(x)
