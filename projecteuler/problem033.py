#coding: utf-8

def main():
    for numerator in range(10, 100):
        for denominator in range(numerator+1, 100):
            if denominator%10 != 0:
                if numerator%10 == denominator//10:
                    exchange = (numerator//10)/(denominator%10)
                    if numerator/denominator == exchange:
                        print(numerator, denominator)
                if numerator//10 == denominator%10:
                    exchange = (numerator%10)/(denominator//10)
                    if numerator/denominator == exchange:
                        print(numerator, denominator)

if __name__ == '__main__':
    main()
