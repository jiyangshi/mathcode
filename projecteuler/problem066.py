#coding: utf-8

import math

def isSquare(nr):
    delta = nr
    sqrt  = int(math.sqrt(delta))
    return delta == sqrt**2

def diophantineEquation(D):
    x      = 2
    ySquare = float(x**2 - 1) / D
    while (round(ySquare) <> ySquare or
            not isSquare(ySquare)):
        x       = x + 1
        ySquare = float(x**2 - 1) / D
    
    return x

if __name__ == '__main__':
    res     = 0
    largest = 0
    for i in range(2, 1001):
        if not isSquare(i):
            middle  = diophantineEquation(i)
            if middle > res:
                res     = middle
                largest = i
    print("largest: %d\n" %largest)
