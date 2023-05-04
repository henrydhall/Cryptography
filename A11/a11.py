#Henry Hall A11

import random

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

def extended_euclidean(a,b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclidean(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

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

def miller_rabin_test(n, a):
    # n: number to test
    # a: potenetial witness
    # returns bool: true if n is composite
    if n % 2 == 0 or extended_euclidean(n,a)[0] != 1:
        return True
    n_1 = n - 1
    k = 0
    while n_1 % 2 == 0:
        k = k+1
        n_1 = n_1 // 2
    a = fast_power(n, a, n_1)
    if a == 1:
        return False
    for i in range(0,n_1):
        if a % n == n - 1:
            return False
        a = a**2 % n
    return True

def miller_rabin_test_many( n ):
    witnesses = [ random.randint( 3, n // 3 ) for i in range(0,10 ) ]
    for i in witnesses:
        if miller_rabin_test(n, i) == True:
            return True, i
    return False, witnesses

def mr_problem():
    print(1105, miller_rabin_test(1105,10))
    print(1105, miller_rabin_test_many(1105))
    print(294409, miller_rabin_test_many(294409))
    print(294439, miller_rabin_test_many(294439))
    print(118901509, miller_rabin_test_many(118901509))
    print(118901521, miller_rabin_test_many(118901521))
    print(118901527, miller_rabin_test_many(118901527))
    print(118915387, miller_rabin_test_many(118915387))

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
    #mr_problem()
    #p_problem()
    print( fast_power(3, 4, 561) )

    #INPUT: N, g, A
    #Solves g^a mod n

