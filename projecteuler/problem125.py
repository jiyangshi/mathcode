"""
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not include as this problems is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
"""


#!/usr/bin/env python


import math
import numpy as np



def is_palindromic(alist):
    """
    alist: A list, like alist = [1, 2 ,3 ,4, 5]

    we check that whether alist is or not palindromic,
    and return ture if it is and return false if it is not.
    """
    return alist[::-1] == alist


def main(N):
    """
    N: Upper Number

    Function that return the sum of have the properties that
    described, blew the number N
    """
    result = 0
    upper = int(math.sqrt(N)) + 1
    for i in range(1, upper):
        for j in range(i+1, upper):
            check = int(sum(pow(np.linspace(i, j, j - i + 1), 2)))
            if check > N:
                break
            else:
                if is_palindromic(list(str(check))):
                    result += check
    return result



if __name__ == '__main__':
    print main(1000)
