#coding: utf-8

def fibonacci(nr):
    a, b, cnt = 1, 1, 1
    while cnt <= nr - 2:
        a, b = b, a + b
        cnt += 1
    return b

def main():
    i, fib = 2750, fibonacci(2750)
    std = ['1', '2', '3', '4', '5', 
            '6', '7', '8', '9']
    
    while ( not sorted(str(fib)[0:9]) == std or
            not sorted(str(fib)[-1:-10:-1]) == std ):
        i += 1
        fib = fibonacci(i)
    
    print ("the smallest fibonacci number that satisfying the condition %d\n" %i)


if __name__ == '__main__':
    main()
