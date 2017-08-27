#coding: utf-8

def problem097s():
    res = 1
    for i in range(7830457):
        res <<= 1
        res  %= 10000000000;
    res *= 28433
    res %= 10000000000
    res += 1
    print (res)

if __name__ == '__main__':
    problem097s()
