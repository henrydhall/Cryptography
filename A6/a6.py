#TODO: shanks and prime number generator

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

def order(p,n):
    for i in range(1,p):
        if fast_power(p, n, i) == 1:
            return i
    else:
        raise ValueError('Could not calculate order')

def shanks(p, g, h):
    x = order(p, g)
    n = int(1 + math.sqrt(x))//1
    u = ee_multiplicative_inverse(p, fast_power(p, g, n) )
    list1 = [ (g**i)%p for i in range(1,n+1) ]
    list2 = [ h*( u**i )%p for i in range(1,n+1) ]
    print(list1)
    print(list2)
    print(n)
    pass

def prime_number_gen(n):
    print(n)

if __name__ == '__main__':
    shanks(17389, 9704, 13896)