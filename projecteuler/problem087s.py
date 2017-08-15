#coding: utf8

def getPrime(limit):
    prime = [2]
    isPrime = True

    for i in range(2, limit):
        isPrime = True
        for p in prime:
            if i%p == 0:
                isPrime = False
                break
        if isPrime == True:
            prime.append(i)
    return prime

def main(nr = 5e7):
    set = {}
    PI = getPrime(int(nr**0.5)+1)
    PJ = getPrime(int(nr**0.33)+1)
    PK = getPrime(int(nr**0.25)+1)
    for pi in PK:
        p1 = pi**4
        if p1 > nr: break
        for pj in PJ:
            p2 = pj**3
            if p2 > nr: break
            for pk in PI:
                p3 = pk**2
                if p3 > nr: break
                if p1 + p2 + p3 < nr:
                    set[p1+p2+p3] = 1
    print(len(set))

if __name__ == '__main__':
    main()
