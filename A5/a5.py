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
    product = (n) % p
    for i in range(1,p):
        if product == 1: 
            return i
        else:
            product = (product * n) % p
    raise ValueError('Could not calculate order')

def shanks(p, g, h):
    x = order(p, g)
    n = int(1 + math.sqrt(x))//1
    u = ee_multiplicative_inverse(p, fast_power(p, g, n) )
    list1 = [ (g**i)%p for i in range(1,n+1) ]
    list2 = [ h*( u**i )%p for i in range(1,n+1) ]
    duplicate = 0
    for item in list1:
        if item in list2:
            duplicate = item
    index1 = list1.index(duplicate) + 1
    index2 = list2.index(duplicate) + 1
    return index1 + (n*index2)

def n_primes(n):
    threes = 9
    primes = [2]
    num_primes = 1
    isPrime = True
    i = 3
    while num_primes != n:
        if i == threes:
            threes += 6
            i += 2
        checkLimit = int( math.sqrt(i)+1 )
        for j in primes:
            if j > checkLimit:
                break
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            num_primes = num_primes + 1
            primes.append(i)
        isPrime = True
        i += 2
    return primes

if __name__ == '__main__':
    print( shanks(17389, 9704, 13896) )
    print(n_primes(10000)[-1])
    print('The millionth prime is 15485863, but it took a minute to get to there...')