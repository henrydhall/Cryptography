#a12 Henry Hall

def extended_euclidean(a,b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = extended_euclidean(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

def fast_power(N, g, A):
    """
    INPUT: N, g, A
    Solves g^a mod n
    """
    #solves (g^a) mod n
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a) % N
        a = (a**2) % N
        A = A//2
    return b

def prime_factors(n):
    i = 2
    limit = n/2
    factors = []
    while i < limit and n != 1:
        if n % i == 0:
            n = n / i
            power = 1
            while n % i == 0:
                n = n / i
                power = power + 1
            factors.append( (i, power) )
        i = i+1
    if n != 1:
        factors.append((int(n), 1))
    return factors

def mersenn_primes(n):
    primes = 0
    i = 2
    while primes < 7:
        factors = prime_factors( 2**i - 1 )
        if len(factors) == 1:
            print( 2**i - 1, ' factors: ', factors )
            primes = primes + 1
        i = i + 1

def pollards( n ):
    a = 2
    for i in range(2, n//2):
        a = fast_power(n, a, i)
        d = extended_euclidean(a-1,n)[0]
        if d != n and d != 1:
            return d, n//d, prime_factors(d-1), prime_factors(n//d - 1)

def p_problem():
    print( pollards(1739) )
    print( pollards(220459) )
    print( pollards(48356747) )

if __name__ == '__main__':
    mersenn_primes(10)