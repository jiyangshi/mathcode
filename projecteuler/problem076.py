#coding: utf-8

import numpy as np

def countingSummations(num):
    matrix = np.ones([num, num])
    for i in range(2, num):
        for j in range(2, num):
            if j < i:
                matrix[i, j] = (
                    matrix[i, j-1] +
                    matrix[i-j, j])
                if (i-j) < j:
                    matrix[i, j] += 1
            elif j == i:
                matrix[i, i] = matrix[i, i-1] + 1
            else:
                matrix[i, j] = matrix[i, i]
    return int(matrix[num-1, num-1])

if __name__ == '__main__':
    print(countingSummations(100))
