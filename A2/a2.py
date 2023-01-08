"""
a2.py
Assignment 2 - Henry Hall
"""

# Problem 1.24 - The Fast Power Algorithm
def fast_power(N, g, A):
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a) % N
        a = (a**2) % N
        A = A//2
    return b

if __name__ == '__main__':
    print( fast_power(21, 9, 30) )