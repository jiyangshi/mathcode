#slightly faster now; less adding/subtracting of powers of 10
#also ensured that ten_pow contains enough powers of 10 
#(way more than enough for large n).
def memoize( f ):
    memo = {}
    def helper( *x ):
        if x not in memo: memo[x] = f(*x)
        return memo[x]
    return helper


def do( n=10**15 ):
    ten_pow=tuple([10**i for i in range(2*len(str(n))+1)])
    @memoize
    def f(d, init=1, carry=0):
        '''f(d) = (init, step), with $a_{step-1}$ = 10**d + init and init (and
        step) as small as possible.'''
        if d == 1:
            x, i = init, 0
            while x < 10:
                x += x + carry
                i += 1
            return x - 10, i
        step = 0
        for _ in range(10):
            new_val, new_ind = f(d - 1, init, carry)
            step += new_ind
            carry += 1
            init = new_val
        return init, step
    new = (1, 0)
    for d in range(1, len(ten_pow)):
        new, old = f(d), new
        #print(d, new)
        if new[1] >= n: break
    d -= 1
    step, init, start_digits = old[1], old[0], ten_pow[d]
    for d in range(d, 0, -1):
        for _ in range(1, 10):
            carry = sum(map(int, str(start_digits)))
            new_val, new_ind = f(d, init, carry)
            if step + new_ind >= n: break
            step += new_ind
            start_digits += ten_pow[d]
            init = new_val
        #print(start_digits + init, step)
    ans = start_digits + init
    for _ in range(n - 1 - step): ans += sum(map(int, str(ans)))
    return ans

print( do(10**17) )
