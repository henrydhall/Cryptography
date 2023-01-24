"""
a3.py
Assignment 3 - Henry Hall
"""

def extended_euclidean(a,b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = extended_euclidean(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

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

def ee_multiplicative_inverse(p,a):
    mi = extended_euclidean(p, a)[2]
    if mi < 0:
        mi = mi + p
    return mi

def fp_multiplicative_inverse(p,a):
    return fast_power(p, a, p-2) 

def euler_totient(a):
    total = 0
    for i in range(a):
        if extended_euclidean(i, a)[0] == 1:
            total = total + 1
    return total

def primitive_root(a,n,psi):
    roots = set()
    for i in range(n):
        roots.add( (a**i)%n )
    print(roots)
    #TODO: need to add a thing to get all elements of F_n            

def primitive_roots(a):
    psi_a = euler_totient(a-1)
    for i in range( a ):
        roots = set()
        for j in range(a):
            roots.add( (i**j) % a)
        if len(roots) == psi_a:
            return roots, len(roots), i
        print(len(roots))
    return 'Failed' # Totally different
 

if __name__ == '__main__':
    print(ee_multiplicative_inverse(47, 11))
    print(fp_multiplicative_inverse(47, 11))

    print(ee_multiplicative_inverse(587, 345))
    print(fp_multiplicative_inverse(587, 345))

    """
    print('\n1.32')
    print('phi(229) = ',euler_totient(228))
    print('Roots: ' , primitive_roots(229))
    """
    print('\nTest')
    print('psi(11) = ', euler_totient(10))
    primitive_root(2,11)
