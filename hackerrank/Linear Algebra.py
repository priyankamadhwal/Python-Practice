import numpy

def main():
    N = int(input())
    mat = []
    for i in range (N):
        mat.append(list(map(float,input().split())))
    print (round(numpy.linalg.det(mat),2))

if __name__ == '__main__':
    main()
