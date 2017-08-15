#coding: utf8

def main():
    x, y = [], []
    
    for n in range(1,28124):
        Sum = 0
        for i in range(1,int(n/2)+1):
            if n % i == 0:
                Sum += i
        if Sum > n:
            x.append(n)
    length = len(x)
    for i in range(length):
        for j in range(i, length):
            temp = x[i] + x[j]
            if temp < 28124:
                y.append(temp)
    y = set(y)

    num = sum(range(1, 28124)) - sum(y)
    print num

if __name__ == '__main__':
    main()
