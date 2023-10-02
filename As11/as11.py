'''
Henry Hall
5.4
9/14/23
'''

import random

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

def fast_power(N, g, A):
    '''
    solves (g^a) mod n
    '''
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a) % N
        a = (a**2) % N
        A = A//2
    return b

class EllipticCurve:
    def __init__(self, A_, B_):
        self.A = A_
        self.B = B_

    def y_squared(self, x_):
        return (x_**3) + (self.A * x_) + self.B

class EllipticCurveField:
    def __init__(self, A_, B_, P_):
        self.Curve = EllipticCurve(A_, B_)
        self.P = P_
        self.finite_field = None

    def get_field_square(self):
        field = dict()
        for i in range(0,self.P):
            field[i] = (i**2) % self.P
        return field
    
    def get_finite_field(self):

        if self.finite_field is not None:
            return self.finite_field

        group_square = self.get_field_square()
        finite_field = ['O']
        for i in range(0,self.P):
            if self.Curve.y_squared(i) % self.P in group_square.values():
                for key in group_square.keys():
                    if group_square[key] == self.Curve.y_squared(i) % self.P:
                        finite_field.append((i,key))
        self.finite_field = finite_field
        return finite_field
    
    def valid_point(self, P) -> bool:
        x, y = P[0], P[1]
        y_test = self.Curve.y_squared(x) % self.P
        y_act = ee_multiplicative_inverse(self.P,y_test)
        y_other = self.P - y_act % self.P
        return y_act == y or y_other == y
    
    def add_points(self, pos1, pos2):

        finite_field = self.get_finite_field()

        if type(pos1) is int:
            value1, value2 = finite_field[pos1], finite_field[pos2]
        else:
            value1, value2 = pos1, pos2

        # A, B
        if value1 == 'O':
            return value2
        elif value2 == 'O':
            return value1
        
        # C
        x1, y1 = value1[0], value1[1]
        x2, y2 = value2[0], value2[1]

        # D
        if x1 == x2 and y1 != y2:
            return 'O'
        
        # E
        if value1 != value2:
            bottom = x2-x1 
            if bottom < 0:
                bottom = bottom + self.P
            bottom = ee_multiplicative_inverse(self.P, bottom)
            lam = bottom * (y2 - y1)
        else:
            bottom = 2*y1
            bottom = ee_multiplicative_inverse(self.P, bottom)
            lam = (3* (x1**2) + self.Curve.A ) * bottom
 
        v = y1 - (lam * x1)

        x3 = (lam**2 - x1 - x2) % self.P
        y3 = (-(lam*x3 + v)) % self.P

        # Checking for finite field trick
        # TODO: don't worry about the finite field, just check if points are valid
        if not self.valid_point((x3,y3)):
            return 'O'

        return (x3, y3)
    
    def get_addition_table(self):
        finite_field = self.get_finite_field()
        print('         ' + str(finite_field))
        for i in range(0,len(finite_field)):
            group = []
            for j in range(0,len(finite_field)):
                group.append( self.add_points(i,j) )
            print(str(finite_field[i]).rjust(6) ,group)

    def brute_force(self, P, Q, max = 150):
        i = 1
        pi = P
        while i < max:
            if pi == Q:
                print(pi,Q)
                return i
            i += 1
            pi = self.add_points(pi,P)

    def double_and_add(self, p, n):
        Q = p
        R = 'O'
        while n > 0:
            if (n-1)%2 == 0:
                R = self.add_points(R,Q)

            Q = self.add_points(Q,Q)
            n = (n // 2)

        return R
    
    def shared_value_from_x(self, alice_x, my_x):
        y_b_2 = self.Curve.y_squared(alice_x)
        y_b = fast_power(self.P, y_b_2, (self.P + 1) / 4 )
        return self.double_and_add((alice_x,y_b),my_x)[0]

def elliptic_curve_factorization( N ):
    A, a, b = random.randint(0,N), random.randint(0,N), random.randint(0,N)
    P = (a,b)
    B = ((b**2)-(a**3)-(A*a)) % N
    ecf = EllipticCurveField(A,B,N)
    print(ecf.valid_point(P)) # TODO: figure out what the heck is going on

if __name__ == '__main__':
    print( elliptic_curve_factorization( 10 ) )