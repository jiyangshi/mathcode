#coding: utf-8

import math

def isSquare(num):
    Sqrt = int(math.sqrt(num))
    return Sqrt**2 == num


def diophantineEquation(D):
    a, b = int(math.sqrt(D)), 1
    k    = a**2 - D * b**2

    while k <> 1:
        msuit = []
        mstd  = []
        for m in range(1, int(math.sqrt(D)+1)):
            if (a + b*m)%k == 0:
                msuit.append(m)
                mstd.append(abs(m**2 - D))
        # Compute the minimal element of mstd
        # minimal_index = mstd.index(min(mstd))
        m = msuit[mstd.index(min(mstd))]
        
        # Update the a, b, k
        a, b = (a*m + D*b)/abs(k), (a + b*m)/abs(k)
        k = (m**2 - D)  / k

    return a, b, k

if __name__ == '__main__':
    alargest = 0
    Dlargest = 0
    for D in range(2, 1001):
        if not isSquare(D):
            a, b, k = diophantineEquation(D)
            if a > alargest:
                alargest = a
                Dlargest = D
    print("Dlargest: %d and alargest: %d\n" 
            %(Dlargest, alargest))
