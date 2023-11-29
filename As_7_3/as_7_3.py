
'''
Henry Hall
M4750 Assignment 7.3
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

def elgamal_dsa(p,g,s,D,e):
    v = fast_power(p,g,s)
    print(v)

    S_1 = fast_power(p,g,e)
    S_2 = (D - (s*S_1)) * ee_multiplicative_inverse(p-1,e) % (p-1)

    print(S_1, S_2)

def prob_7_4():
    #elgamal_dsa(21739,7,15140,5331,10727)
    elgamal_dsa(6961,437,6104,5584,4451)

def elgamal_verify(p,g,v,D,S_1,S_2):
    eq_1 = (fast_power(p,v,S_1)*fast_power(p,S_1,S_2)) % p
    eq_2 = fast_power(p,g,D)
    print(eq_1==eq_2)

def prob_7_5():
    elgamal_verify(6961,437,4250,1521,4129,5575)
    elgamal_verify(6961,437,4250,1837,3145,1871)
    elgamal_verify(6961,437,4250,1614,2709,2994)

def dsa(p,q,g,s,D,e):
    v = fast_power(p,g,s)
    print(v)
    S_1 = fast_power(p,g,e) % q
    #print(D,s,S_1,ee_multiplicative_inverse(q,e),q)
    S_2 = ((D + (s*S_1)) * ee_multiplicative_inverse(q,e)) % q
    print(S_1,S_2)

def prob_7_8():
    #dsa(48731,443,5260,242,343,427)
    dsa(22531,751,4488,674,224,574)

def dsa_verify(p,q,g,v,D,S_1,S_2):
    V_1 = (D * ee_multiplicative_inverse(q,S_2)) % q
    V_2 = S_1 * ee_multiplicative_inverse(q,S_2) % q
    eq = int( ( (g**V_1) % p * (v**V_2) % p ) % q )
    print(eq == S_1)

def prob_7_9():
    #dsa_verify(48731,443,5260,3438,343,59,166)
    #dsa_verify(22531,751,4488,4940,244,444,56)
    dsa_verify(22531,751,4488,22476,329,183,260)
    dsa_verify(22531,751,4488,22476,432,211,97)

import as11

# TODO: 7.12
def ecdsa(p,a,b,G,q,s,d,e):
    my_curve = as11.EllipticCurveField(a,b,p)
    print(my_curve.is_point(G))
    # Key Creation
    V = my_curve.double_and_add(G,s)
    print(V)

    # Signing
    egg = my_curve.double_and_add(G,e)
    s_1 = egg[0] % q
    s_2 = ((d + (s*s_1)) * ee_multiplicative_inverse(q,e)) % q
    print(s_1,s_2)

def prob_7_12a():
    ecdsa(17389,231,473,(11259,11278),1321,542,644,847)

def ecdsa_verify(a,b,G,p,q,s_1,s_2,d,v):
    my_curve = as11.EllipticCurveField(a,b,p)
    v_1 = d * ee_multiplicative_inverse(q, s_2) % q
    v_2 = s_1 * ee_multiplicative_inverse(q,s_2) % q
    v_3 = my_curve.double_and_add(G,v_1)
    v_4 = my_curve.double_and_add(v,v_2)
    v_f = my_curve.add_points( v_3, v_4 )
    print(v_f[0] % q == s_1 % q)
    pass

def prob_7_12b():
    ecdsa_verify(231,473,(11259,11278),17389,1321,907,296,993,(11017,14637))
    pass

def prob_7_7():
    p = 348149
    g = 113459
    v = 185149

    D = 153405
    s_1 = 208913
    s_2 = 209176
    
    D_p = 127561
    s_2_p = 217800

    e_1 = ((s_1 * (s_2_p - s_2) )) % (p - 1)
    e_2 = ((s_2_p * D) - (s_2 * D_p)) % (p - 1)

    e_2 = (ee_multiplicative_inverse(p-1,e_1) * e_2) % (p - 1)

    denom = extended_euclidean(e_1,p-1)[0]

    print(e_2/denom)
    print(fast_power(p,g,e_2/denom),v)

if __name__ == '__main__':
    pass
    #prob_7_4()
    #prob_7_5()
    #prob_7_7()
    #prob_7_8()
    #prob_7_9()
    #prob_7_12a()
    #prob_7_12b()
