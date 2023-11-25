'''
Henry Hall
5.5
10/7/23
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

class EllipticCurve:
    def __init__(self, A_, B_):
        self.A = A_
        self.B = B_

    def y_squared(self, x_):
        return (x_**3) + (self.A * x_) + self.B
    
    def add(self, p, q):

        value1, value2 = p, q

        # A, B
        if value1 == 'O':
            return value2
        elif value2 == 'O':
            return value1
        
        # C
        x1, y1 = value1[0], value1[1]
        x2, y2 = value2[0], value2[1]

        # D
        if x1 == x2 and y1 == -y2:
            return 'O'
        
        # E
        if value1 != value2:
            lam = (y2-y1) / (x2-x1)
        else:
            lam = ((3*(x1**2)) + self.A) / (2*y1)
 
        x3 = (lam**2 - x1 - x2) 
        y3 = (lam * (x1 - x3)) - y1

        return (x3, y3)
    
class EllipticCurveField:
    def __init__(self, A_, B_, P_):
        self.Curve = EllipticCurve(A_, B_)
        self.P = P_

    def add_points(self, p, q):
        value1, value2 = p, q

        # A, B
        if value1 == 'O':
            return value2
        elif value2 == 'O':
            return value1
        
        # C
        x1, y1 = value1[0], value1[1]
        x2, y2 = value2[0], value2[1]

        # D
        if x1 == x2 and y1 == -y2:
            return 'O'
        
        # E
        if value1 != value2:
            lam = (y2-y1) * ee_multiplicative_inverse(self.P,x2-x1)
        else:
            lam = ((3*(x1**2)) + self.Curve.A) * ee_multiplicative_inverse(self.P,2*y1)
 
        x3 = (lam**2 - x1 - x2) 
        y3 = (lam * (x1 - x3)) - y1

        # TODO: make sure the point is valid
        return (x3%self.P, y3%self.P)

    
    def double_and_add(self, p, n):
        Q = p
        R = 'O'
        while n > 0:
            if (n-1)%2 == 0:
                R = self.add_points(R,Q)

            Q = self.add_points(Q,Q)
            n = (n // 2)

        return R
    
    
    def lenstra_add(self, p, q):
        value1, value2 = p, q

        # A, B
        if value1 == 'O':
            return value2
        elif value2 == 'O':
            return value1
        
        # C
        print(type(value1))
        x1, y1 = value1[0], value1[1]
        x2, y2 = value2[0], value2[1]

        # D
        if x1 == x2 and y1 == -y2:
            return 'O'
                
        # E

        gcd = extended_euclidean(x2-x1,self.P)[0]

        if gcd not in [0,1,-1,self.P]:
            return gcd
            
        if value1 != value2:
            lam = (y2-y1) * ee_multiplicative_inverse(self.P,x2-x1)
        else:
            lam = ((3*(x1**2)) + self.Curve.A) * ee_multiplicative_inverse(self.P,2*y1)

        x3 = (lam**2 - x1 - x2) 
        y3 = (lam * (x1 - x3)) - y1

        return (x3%self.P, y3%self.P)
    
    def lenstra_double_and_add(self, p, n):
        Q = p
        R = 'O'

        while n > 0:
            if (n-1)%2 == 0:
                R = self.lenstra_add(R,Q)
                if type(R) == 'long':
                    return R

            Q = self.lenstra_add(Q,Q)
            n = (n // 2)

            if type(Q) == 'long':
                return Q
        return R
        
    def lenstra_factor(self, P, max_mult ):
        # Functions in class to allow for factoring
        '''
        Using Lenstra's to factor p
        '''
        p = P

        for i in range(2,max_mult):
            P = self.lenstra_double_and_add(P,i)
            if type(P) is int:
                return P
            
    def is_point(self,P):
        pass
        # TODO: implement this.
    
def lenstra_factorization(n, max_curve, max_mult):
    '''
    n int: number to attempt factoring.
    m int: number of curves to attempt with.
    '''
    # Functions out of class to do factoring
    
    for i in range(0, max_curve):
        P = (random.randint(1,n),random.randint(1,n))
        a = P[0]
        b = P[1]
        A = random.randint(0,n)
        B = ((b**2) - (a**3) - (A*a)) % n
        curve = EllipticCurveField(A,B,n)

        possible = curve.lenstra_factor(P,max_mult) 
        if possible:
            return possible
    
def curve_tester():
    my_curve = EllipticCurve(-15,18)
    print(my_curve.add( (7,16),(1,2) ))

    my_curve = EllipticCurve(-15,18)
    print( my_curve.add((7,16),(7,16)) )
    
def ex_4():
    n = 6887
    P = (1512,3166)
    a = P[0]
    b = P[1]
    A = 14
    B = ((b**2) - (a**3) - (A*a)) % n
    curve = EllipticCurveField(A,B,6887)

    for i in range(1, 8):
        P = curve.double_and_add(P,i)
        print(P[0] % n, P[1] % n)

    
if __name__ == '__main__':
    #ex_4()
    #curve_tester()
    #print( (((1512**3)+(14*1512)+19 ) - (3166**2)) % 6887 )
    print( lenstra_factorization(589,100,15))
    print( lenstra_factorization(26167,100,15))
    print( lenstra_factorization(1386493,100,15))
    print( lenstra_factorization(28102844557,100,15))

