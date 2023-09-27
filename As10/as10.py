'''
Henry Hall
5.4
9/14/23
'''


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
        if (x3,y3) not in finite_field:
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

def prob_5_13():

    ecf = EllipticCurveField(171,853,2671)
    # a
    print(ecf.double_and_add((1980,431),1943))
    # b
    print(ecf.double_and_add((2110,543),1943))
    # c
    print(ecf.brute_force((1980,431),(2110,543),1000))

    # d 
    print( ecf.Curve.y_squared(2) )
    print( ecf.double_and_add((1980,431),875) ) # TODO: get shared value
    print(ecf.shared_value_from_x(2,875))

def MV_Elgamal(P, A, B, point, nA, message):
    '''
    Menezes-Vanstone Elgamal Cryptosystem
    '''
    MVE_Curve = EllipticCurveField( A, B, P )
    QA = MVE_Curve.double_and_add(point, nA)
    print(QA)
    T = MVE_Curve.double_and_add(message[0],nA)
    m1 = ee_multiplicative_inverse(P,T[0]) * message[1] % P
    m2 = ee_multiplicative_inverse(P, T[1]) * message[2] % P
    print(m1, m2)

def prob_5_16():
    MV_Elgamal(1201, 19, 17, (278,285), 595, ((1147,640),279,1189))

if __name__ == '__main__':
    prob_5_16()