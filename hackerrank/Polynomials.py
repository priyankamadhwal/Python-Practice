import numpy

def main():
    coeff = list(map(float,input().split()))
    x = float(input())
    val = numpy.polyval(coeff,x)
    print(val)

if __name__ == '__main__':
    main()
