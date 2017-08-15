#coding: utf8

import time

def main():
    starttime = time.time()
    pSet = set()
    dictionary = {}

    n = 0
    p = 0
    while 1:
        p += 3 * n + 1
        if dictionary.has_key(p):
            print (dictionary[p])
            break

        for old in pSet:
            diff = p - old
            if diff in pSet:
                dictionary[p+old] = diff

        pSet.add(p)
        n += 1

    print ("time: ", time.time() - starttime)

if __name__ == '__main__':
    main()
