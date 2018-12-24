if __name__ == '__main__':
    marksheet = []
    N = int(input())
    marksheet = [[input(),float(input())] for _ in range(N)]
    secondLowest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([name for name,marks in sorted(marksheet) if marks == secondLowest]))
