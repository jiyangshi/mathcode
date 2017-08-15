#coding: utf8


def main():
    product = []
    standard = sorted('123456789')
    for i in range(12, 100):
        for j in range(123, 1000):
            string = str(i) + str(j) + str(i*j)
            if sorted(string) == standard:
                product.append(i*j)
    for i in range(1, 10):
        for j in range(1234, 10000):
            string = str(i) + str(j) + str(i*j)
            if sorted(string) == standard:
                product.append(i*j)
    print ("the sum of all products is %d\n" % sum(set(product)))


if __name__ == '__main__':
    main()
