# Henry Hall
# A10

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

def RSA_breaker(n,e1,e2,c1,c2):
    gcd_e, u, v = extended_euclidean(e1,e2)
    c2 = ee_multiplicative_inverse(n,c2)
    raised_c1 = fast_power(n, c1, u)
    raised_c2 = fast_power(n, c2, -v)
    m = raised_c1 * raised_c2
    return m % n

if __name__ == '__main__':
    print(RSA_breaker(1889570071, 1021763679 , 519424709, 1244183534, 732959706))