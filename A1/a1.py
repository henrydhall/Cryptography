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
 
if __name__ == '__main__':
    print( euclidean(139024789,93278890) )
    print( euclidean( 16534528044, 8332745927) )
    print( extended_euclidean(291, 252) )
    print( extended_euclidean(16261, 85652) )
    print( extended_euclidean(4,7))
