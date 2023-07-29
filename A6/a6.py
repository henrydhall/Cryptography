"""
 Assignment 6
 Henry Hall
"""

import math

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

def brute_force_discrete_log_fast_power(g,h,p):
    # Finds x for g^x = h (mod p)
    for i in range(0,p):
        if fast_power(p, g, i) - h == 0:
            return i
    return 'fail'

def diffie_hellman(p, g):
    # p shared prime
    # g shared base
    a = 1      # Alice's, unknown a
    b = 871    # Bob's picked b
    A = 974    # Alice's sent A
    B = 1      # Bob's 

    B = fast_power(p, g, b)
    shared = fast_power(p, A, b)

    a = brute_force_discrete_log_fast_power(g, 974, p)

    return B, shared, a

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

def Elgamal(P, g, a, b, m, k):
    """
    Elgamal(P, g, a, b, m, k)
    Input: 
        P: public prime key
        g: public base
        a: receiver secret key
        b: sender secret key
        m: sender message
        k: ephemeral key
    """

    #P     # Public prime
    #g     # Public root of large prime order

    # Key creation
    #a    # Selected private key
    A = fast_power(P, g, a) # Public key
    print(f'A: {A}')

    # Encryption
    #m # Plaintext
    #k # Ephemeral key
    c1 = fast_power(P, g, k)
    c2 = (m * fast_power(P, A, k) ) % P
    print('Message: ', (c1,c2))

    # Decryption
    x = fast_power(P, c1, a)
    x_1 = ee_multiplicative_inverse(P,x)
    m_d = (x_1 * c2)%P
    print(m_d)

def Elgamal_decrypt(P, g, a, message):
    """
    Elgamal(P, g, a, b, m, k)
    Input: 
        P: public prime key
        g: public base
        a: receiver secret key
        message: sender message
    """
    c1 = message[0]
    c2 = message[1]

    x = fast_power(P, c1, a)
    x_1 = ee_multiplicative_inverse(P,x)
    m_d = (x_1 * c2)%P
    print(m_d)

def Elgamal_eavesdrop(P, g, B, message):
    a = brute_force_discrete_log_fast_power(g,B,P)
    print(a)

    c1 = message[0]
    c2 = message[1]


    x = fast_power(P, c1, a)
    x_1 = ee_multiplicative_inverse(P,x)
    m_d = (x_1 * c2)%P
    print(m_d)

if __name__ == '__main__':
    #print(diffie_hellman(1373, 2))
    #print(Elgamal(1373, 2, 716, 947, 583, 877))
    #Elgamal(1373, 2, 716, 947, 583, 877)
    #Elgamal(1373, 2, 299, b, m, k)
    #Elgamal_decrypt(1373, 2, 299, (661,1325))
    #Elgamal_eavesdrop(1373, 2, 893, (693,793))
    print( ee_multiplicative_inverse(11, 90) )