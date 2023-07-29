"""
Assignment 5, Fall 2023 Cryptography Course
Henry Hall
"""

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
    """solves (g^a) mod n"""
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a) % N
        a = (a**2) % N
        A = A//2
    return b

if __name__ == '__main__':
    print( f'GCD of 13974, 19110 = {extended_euclidean(13974,19110)}' )
    print( ee_multiplicative_inverse(81798,19110) )
    i = 10325
    while fast_power(81799,11,i) != 41387:
        i += 13633
    print(i)