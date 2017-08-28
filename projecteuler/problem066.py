#coding: utf-8

import math

def isSquare(num):
    sqrt  = int(math.sqrt(num))
    return num == sqrt**2

xlargest = 0
Dlargest = 0
for D in range(2, 1001):
    if not isSquare(D):
        y       = 1
        xSquare = 1 + D * y**2
        Sqrt    = int(math.sqrt(xSquare))

        while Sqrt**2 <> xSquare:
            y       = y + 1
            xSquare = 1 + D * y**2
            Sqrt    = int(math.sqrt(xSquare))

        if Sqrt > xlargest:
            xlargest = Sqrt
            Dlargest = D

print("Dlargest: %d\n" %Dlargest)
