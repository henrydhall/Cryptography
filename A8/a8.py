# A8

import math

def extended_euclidean(a,b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = extended_euclidean(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

def ee_multiplicative_inverse(p,a):
    mi = extended_euclidean(p, a)[2]
    if mi < 0:
        mi = mi + p
    return mi

def fp_multiplicative_inverse(p,a):
    return fast_power(p, a, p-2) 

def fast_power(N, g, A):
    #solves (g^a) mod n
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a) % N
        a = (a**2) % N
        A = A//2
    return b

def congruence_solver_1(p,m,e):
    for i in range(0,1000):
        if fast_power(p, i, e) == m:
            return i
    return 'bust'

def congruence_solver_fast(p,m,e):
    d = ee_multiplicative_inverse( p-1, e )
    x = fast_power( p, m, d )
    return x

def congruence_solver_comp(p,m,e,composites):
    product = 1
    for c in composites:
        product = product * (c-1)
    d = ee_multiplicative_inverse( product, e )
    x = fast_power( p, m, d )
    return x

def euler_totient(a):
    total = 0
    for i in range(a):
        if extended_euclidean(i, a)[0] == 1:
            total = total + 1
    return total

def funky_euler(N, divisors):
    product = 1
    #TODO: this
    #Phi(n) = N*(Product of 1 - (1/p) for all p that divide N)
    for i in divisors:
        product = product * (1-(1/i))
    return int(product * N)

def prime_factors(n):
    i = 2
    limit = math.sqrt(n)
    factors = []
    while i < limit and n != 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
            while n % i == 0:
                n = n / i
        i = i+1
    return factors

if __name__ == '__main__':
    pass
    """
    print( congruence_solver_fast(541,428,137) )
    print( congruence_solver_fast(97,36,19) )
    print( congruence_solver_comp(1159,614,73,[61,19]) )
    print( congruence_solver_comp(8023,677,751,[71,113]) )
    print( congruence_solver_comp(401227,328047,38993,[607,661]) )
    """
    """
    print(euler_totient(17))
    print(euler_totient(23))
    print(euler_totient(17)*euler_totient(23))
    print(euler_totient(17*23))
    """
    """
    print( euler_totient(13) )
    print( euler_totient(13**2) )
    print( euler_totient(13**3) )
    print( euler_totient(13**4) )
    print(12)
    print(13*12)
    print(13**2 * 12)
    print(13**3 * 12)
    print(13**2)
    print(13**3)
    """
    print( funky_euler(1728, prime_factors(1728)) )
    print( funky_euler(1575, prime_factors(1575)) )
    print( funky_euler(889056,[2,3,7]))


