#coding: utf-8

import math

def is_prime(nr):
    for i in range(2, int(math.sqrt(nr))+1):
        if nr%i == 0:
            return False
    return True

"""
def special_sum(i, j, k):
    return i**2 + j**3 + k**4
"""
def special_count(nr = 5e7):
    
    ni = int(nr**0.5) + 1
    nj = int(nr**0.33) + 1
    nk = int(nr**0.25) + 1

    ai = []; aj = []; ak = []
    for i in range(2, ni):
        if is_prime(i):
            ai.append(i)
    for j in range(2, nj):
        if is_prime(j):
            aj.append(j)
    for k in range(2, nk):
        if is_prime(k):
            ak.append(k)
    
    special_num = []
    for i in ai:
        for j in aj:
            for k in ak:
                value = i**2 + j**3 + k**4
                if value < nr:
                    special_num.append(value)

    print ("the number of special number is %d" %(len(set(special_num))))


if __name__ == '__main__':
    special_count()
