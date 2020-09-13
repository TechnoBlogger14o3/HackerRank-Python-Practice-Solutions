import numpy


poly = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(poly, x))
