'''
Henry Hall
5.5
10/7/23
'''

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

        # Checking for finite field trick
        return (x3, y3)
    
    def double_and_add(self, p, n):
        Q = p
        R = 'O'
        while n > 0:
            if (n-1)%2 == 0:
                R = self.add_points(R,Q)

            Q = self.add_points(Q,Q)
            n = (n // 2)

        return R
    
def curve_tester():
    my_curve = EllipticCurve(-15,18)
    print(my_curve.add( (7,16),(1,2) ))

    my_curve = EllipticCurve(-15,18)
    print( my_curve.add((7,16),(7,16)) )
    
def elliptic_curve_factorization(n):
    pass
    
def ex_4():
    n = 6887
    P = (1512,3166)
    a = P[0]
    b = P[1]
    A = 14
    B = ((b**2) - (a**3) - (A*a)) % n
    curve = EllipticCurve(A,B)
    p2 = curve.add(P,P)
    print(p2[0] % n, p2[1] % n)
    
if __name__ == '__main__':
    #ex_4()
    curve_tester()
    #print( (((1512**3)+(14*1512)+19 ) - (3166**2)) % 6887 )