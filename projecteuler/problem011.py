"""
file: problem011.py
To solve the small question
that need that ability to handle
the I/O question
"""

#coding: utf-8

import pandas as pd

data = pd.read_csv('problem011.csv').values

# up conditions
def up():
    Max = 0
    for i in xrange(3, 20):
        for j in xrange(0, 20):
            mid = (data[i, j]*data[i-1, j]*
                   data[i-2, j]*data[i-3, j])
            if mid > Max:
                Max = mid
    return Max

# down conditions
def down():
    Max = 0
    for i in xrange(0, 17):
        for j in xrange(0, 20):
            mid = (data[i, j]*data[i+1, j]*
                   data[i+2, j]*data[i+3, j])
            if mid > Max:
                Max = mid
    return Max

# left conditions
def left():
    Max = 0
    for i in xrange(0, 20):
        for j in xrange(3, 20):
            mid = (data[i, j]*data[i, j-1]*
                   data[i, j-2]*data[i, j-3])
            if mid > Max:
                Max = mid
    return Max

# right conditions
def right():
    Max = 0
    for i in xrange(0, 20):
        for j in xrange(0, 17):
            mid = (data[i, j]*data[i, j+1]*
                   data[i, j+2]*data[i, j+3])
            if mid > Max:
                Max = mid
    return Max


# diagonal conditions
def leftdiagonal():
    Max = 0
    for i in xrange(0, 17):
        for j in xrange(0, 17):
            mid = (data[i, j]*
                   data[i+1, j+1]*
                   data[i+2, j+2]*
                   data[i+3, j+3])
            if mid > Max:
                Max = mid
    return Max

# diagonal conditions
def rightdiagonal():
    Max = 0
    for i in xrange(0, 17):
        for j in xrange(3, 20):
            mid = (data[i, j]*
                   data[i+1, j-1]*
                   data[i+2, j-2]*
                   data[i+3, j-3])
            if mid > Max:
                Max = mid
    return Max

if __name__ == '__main__':
    print(max(up(), down(),
              left(), right(),
              leftdiagonal(),
              rightdiagonal()))
