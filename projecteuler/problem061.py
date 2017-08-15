#coding: utf8

import math

def isTriangle(nr):
    # standard
    delta = 1 + 8 * nr
    sqrt  = int(math.sqrt(delta))
    return (delta == sqrt**2
            and (-1+sqrt)%2 == 0)

def isSquare(nr):
    # standard
    delta = nr
    sqrt  = int(math.sqrt(delta))
    return delta == sqrt**2

def isPentagonal(nr):
    # standard
    delta = 1 + 24 * nr
    sqrt  = int(math.sqrt(delta))
    return (delta == sqrt**2
            and (1+sqrt)%6 == 0)

def isHexagonal(nr):
    # standard
    delta = 1 + 8 * nr
    sqrt  = int(math.sqrt(delta))
    return (delta == sqrt**2
            and (1+sqrt)%4 == 0)


def isHeptagonal(nr):
    # standard
    delta = 9 + 40 * nr
    sqrt  = int(math.sqrt(delta))
    return (delta == sqrt**2
            and (3+sqrt)%10 == 0)

def isOctagonal(nr):
    # standard
    delta = 4 + 12 * nr
    sqrt  = int(math.sqrt(delta))
    return (delta == sqrt**2
            and (2+sqrt)%6 == 0)

def isSpecial(nr):
    return (isTriangle(nr)   or
            isSquare(nr)     or
            isPentagonal(nr) or
            isHexagonal(nr)  or
            isHeptagonal(nr) or
            isOctagonal(nr))

def checkSpecial(nr):
    checkS = []
    if isTriangle(nr):
        checkS.append(1)
    else:
        checkS.append(0)
    if isSquare(nr):
        checkS.append(1)
    else:
        checkS.append(0)
    if isPentagonal(nr):
        checkS.append(1)
    else:
        checkS.append(0)
    if isHexagonal(nr):
        checkS.append(1)
    else:
        checkS.append(0)
    if isHeptagonal(nr):
        checkS.append(1)
    else:
        checkS.append(0)
    if isOctagonal(nr):
        checkS.append(1)
    else:
        checkS.append(0)

    return checkS

def cyclicalFigurateNumbers(nr):
    if not isSpecial(nr):
        return 0
    for i in range(10, 100):
        if isSpecial(int(str(nr)[2:4]+str(i))):
            for j in range(10, 100):
                if isSpecial(int(str(i)+str(j))):
                    for k in range(10, 100):
                        if isSpecial(int(str(j)+str(k))):
                            for p in range(10, 100):
                                if isSpecial(int(str(k)+str(p))):
                                    for q in range(10, 100):
                                        if isSpecial(int(str(p)+str(q))):
                                            if str(q) == str(nr)[0:2]:
                                                Sum = (nr + int(str(nr)[2:4]+str(i)) +
                                                        int(str(i)+str(j))+
                                                        int(str(j)+str(k))+
                                                        int(str(k)+str(p))+
                                                        int(str(p)+str(q)))
                                                print (nr, int(str(nr)[2:4]+str(i)),
                                                        int(str(i)+str(j)),
                                                        int(str(j)+str(k)),
                                                        int(str(k)+str(p)),
                                                        int(str(p)+str(q)))
                                                print checkSpecial(nr)
                                                print checkSpecial(int(str(nr)[2:4]+str(i)))
                                                print checkSpecial(int(str(i)+str(j)))
                                                print checkSpecial(int(str(j)+str(k)))
                                                print checkSpecial(int(str(k)+str(p)))
                                                print checkSpecial(int(str(p)+str(q)))
                                                return Sum
                                    return 0
                            return 0
                    return 0
            return 0
    return 0
if __name__ == '__main__':
    for i in range(1000, 10000):
        Sum = cyclicalFigurateNumbers(i)
        if Sum:
            print Sum
