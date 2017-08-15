#coding: utf8

import itertools

def main():
    alist = []
    for item in itertools.permutations('0123456789'):
        alist.append(int(''.join(item)))
    print ("the millionth lexicographic order is %d\n" 
            % sorted(alist)[1000000-1])

if __name__ == '__main__':
    main()
