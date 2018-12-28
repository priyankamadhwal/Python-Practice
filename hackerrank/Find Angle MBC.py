from math import atan
from math import degrees

AB, BC = int(input()), int(input())
'''
APPROACH: Consider B at origin, then A(0,AB), B(0,0), C(AC,0)
          find slope(BM)
'''
print(str(round(degrees(atan((AB / 2) / (BC / 2))))) + "°")
