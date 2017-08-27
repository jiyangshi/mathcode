#coding: utf-8

import math
import numpy as np

def isPrime(nr):
    if nr == 1:
        return False
    for i in range(2, int(math.sqrt(nr))+1):
        if nr%i == 0:
            return False
    return True


def decompositionNumbers(nr):
    decom1 = []
    decom2 = []
    cnt = 2
    while not isPrime(nr) and nr <> 1:
        if isPrime(cnt) and nr%cnt == 0:
            decom1.append(cnt)
            nr /= cnt
        while isPrime(cnt) and nr%cnt == 0:
            nr /= cnt
            decom2.append(cnt)
        cnt += 1

    if nr <> 1:
        decom1.append(nr)
    return decom1, decom2

if __name__ == '__main__':

    alist = [2, 3, 5, 7, 11, 13, 17]
    print np.prod(alist)
