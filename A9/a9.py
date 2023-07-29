# RSA

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

def prime_factors(n):
    i = 2
    limit = n/2
    factors = []
    while i < limit and n != 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
            while n % i == 0:
                n = n / i
        i = i+1
    return factors

def congruence_solver_comp(p,m,e,composites):
    product = 1
    for c in composites:
        product = product * (c-1)
    d = ee_multiplicative_inverse( product, e )
    x = fast_power( p, m, d )
    return x

def key_creation(p, q, e):
    # Input primes p and q
    # Input encryption exponent e s.t. gcd(e, (p-1)(q-1)) = 1
    # Output N = pq, and e
    if extended_euclidean( e, (p-1)*(q-1) )[0] != 1:
        raise ValueError(f'GCD of {e} and ({p}-1)({q}-1) is not 1')

    return p*q, e

def encrypt(N, e, m):
    return fast_power(N, m, e)

def decrypt(N, e, m, comp):
    mp = congruence_solver_comp( N, m, e, comp )
    return mp

def decryption_exponent( N, e ):
    comp = prime_factors(N)
    product = 1
    for c in comp:
        product = product * (c-1)
    d = ee_multiplicative_inverse( product, e )
    return d

def pq_finder(pq, otherpq):
    ppq = pq - otherpq + 1
    sol1 =  -(-ppq + math.sqrt( (ppq**2) - (4*pq) ))/2
    sol2 =  -(-ppq - math.sqrt( (ppq**2) - (4*pq) ))/2
    return int(sol1), int(sol2)

#TODO: 3.8

if __name__ == '__main__':
    pass
    print(encrypt(2038667 , 103, 892383))
    print(decrypt(2038667, 103, 45293, [1301, 1567]))
    print(decryption_exponent(2038667, 103))
    print(decrypt(2038667,103, 317730, prime_factors(2038667)))
    print(decrypt(12191,37,587, prime_factors(12191)))
    print(pq_finder(352717,351520))
    print(pq_finder(77083921,77066212))
    print(pq_finder(109404161,109380612))
    print(pq_finder(172205490419,172204660344))

