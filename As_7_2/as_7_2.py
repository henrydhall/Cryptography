#!python
'''
Assignment 7.2
M 4750
RSA Digital Signatures
'''

def fast_power(N, g, A):
    '''
    INPUT: N, g, A
    Solves g^A mod N
    '''
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

def ee_multiplicative_inverse(p,a):
    mi = extended_euclidean(p, a)[2]
    if mi < 0:
        mi = mi + p
    return mi

def problem_7_1():
    p = 541
    q = 1223
    v = 159853

    N = p * q

    s = ee_multiplicative_inverse( (p-1)*(q-1), v )
    print(s)

if __name__ == '__main__':
    problem_7_1()
    # TODO: verify this works at all lol