# Assignment 13 - Henry Hall

import math

def extended_euclidean(a,b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = extended_euclidean(b % a, a)
 
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

def factor_by_squares(n):
    i = 0
    while i < 10000:
        square_root = math.sqrt(n + i**2)
        if square_root // 1 == square_root:
            return (square_root + i), (square_root - i)
        i = i + 1

def factor_by_squares_advanced(n,k,b_init):
    for i in range(b_init,10000):
        square_root = math.sqrt( (k*n) + i**2 )
        if square_root // 1 == square_root:
            factor_a = extended_euclidean( n, square_root + i )[0]
            factor_b = extended_euclidean( n, square_root - i)[0]
            return factor_a, factor_b
        i = i + 1
    pass

if __name__ == '__main__':
    print( factor_by_squares(53357) )
    print( factor_by_squares(34571) )
    print( factor_by_squares(25777) )
    print( factor_by_squares(64213) )
    print(factor_by_squares_advanced(143041,247,1))
    print(factor_by_squares_advanced(1226987,3,36))
    print(factor_by_squares_advanced(2510839,21,90))

