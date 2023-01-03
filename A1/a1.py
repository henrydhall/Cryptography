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
#https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/

if __name__ == '__main__':
    print( euclidean(139024789,93278890) )
    print( euclidean( 16534528044, 8332745927) )