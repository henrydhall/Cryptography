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

def rsa_signature_sign(p,q,v,D):
    N = p * q

    s = ee_multiplicative_inverse( (p-1)*(q-1), v )

    S = fast_power(N,D,s)

    print(p*q,s,S)

def rsa_verify(N, v, D, S):
    print( fast_power(N,S,v) == D )

def problem_7_1():
    rsa_signature_sign(541, 1223, 159853,630579)

def problem_7_2():
    rsa_verify(1562501, 87953, 119812, 876453)
    rsa_verify(1562501, 87953, 161153, 870099)
    rsa_verify(1562501, 87953, 586036, 602754)

def problem_7_3():
    N = 27212325191
    v = 22824469379

    i = 3
    while N % i != 0:
        i += 2
    
    print(i, N / i)

    # TODO: finish problem 7.3

if __name__ == '__main__':
    problem_7_3()