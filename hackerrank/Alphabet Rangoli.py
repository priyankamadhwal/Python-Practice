def print_rangoli(size):
    lst = []
    for i in range(size):
        j =  size-1
        alpha = []
        for k in range(i+1):
            alpha.append(chr(97+j))
            j -= 1
        pattern = "-".join(alpha)
        pattern = pattern + pattern[::-1][1:]
        lst.append(pattern.center((2*size-1)+(2*size-2),'-'))
    for i in range(size):
        print(lst[i])
    for i in range(size-2,-1,-1):
        print(lst[i])



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
