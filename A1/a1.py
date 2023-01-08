"""
a1.py
Assignment 1 - Henry Hall
"""

# Problem 1.9 - The Euclidean Algorithm
def euclidean(a,b):
    r_0 = max(a,b)
    r_1 = min(a,b)
    i = 1
    r = [r_0, r_1]
    while r[-1] > 0:
        r.append( r[-2] % r[-1] )

    return r[-2]

# Problem 1.10 - The Extended Euclidean Algorithm
def extended_euclidean(a,b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = extended_euclidean(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

# Problem 1.12 Improved Extended Euclidean Algorithm
def improved_euclidean(a,b):
    # Catching b = 0
    if b == 0:
        return a, 1, 0
    u = 1
    g = a
    x = 0
    y = b
    while y != 0:
        q, t = g//y, g%y
        s = u-(q*x)
        u = x
        g = y
        x = s
        y = t
            
    v = (g-(a*u))/b
    if u <= 0:
        u = u + (b/g)
        v = v - (a/g)
    return g, u, v
    
def prob_1_12():
    print('Prob 1.12')
    print( improved_euclidean(527, 1258) )
    print( improved_euclidean(228, 1056) )
    print( improved_euclidean(163961, 167181) )
    print( improved_euclidean(3892394, 239847) )

    
 
if __name__ == '__main__':
    print( euclidean(139024789,93278890) )
    print( euclidean( 16534528044, 8332745927) )
    print( extended_euclidean(291, 252) )
    print( extended_euclidean(16261, 85652) )
    print( extended_euclidean(4,7))
    print( improved_euclidean(4,7))
    prob_1_12()
