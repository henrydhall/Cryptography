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

if __name__ == '__main__':
    print(ee_multiplicative_inverse(47, 11))
    print(fp_multiplicative_inverse(47, 11))

    print(ee_multiplicative_inverse(587, 345))
    print(fp_multiplicative_inverse(587, 345))