import math
radius = int(input())
def volume(num):
    a = float(math.pi * pow(num, 3) * (4/3))
    print(a)

volume(radius)