if __name__ == '__main__':
    N = int(input())
    distinctCountries = set()
    for _ in range(N):
        distinctCountries.add(input())
    print(len(distinctCountries))
