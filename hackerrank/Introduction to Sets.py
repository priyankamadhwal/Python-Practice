def average(array):
    arrayDistinct = list(set(array))
    return sum(arrayDistinct) / len(arrayDistinct)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
