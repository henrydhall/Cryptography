'''
Henry Hall
8/26/23

Assignment 5.2
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

    def get_field_square(self):
        field = dict()
        for i in range(0,self.P):
            field[i] = (i**2) % self.P
        return field
    
    def get_finite_field(self):
        group_square = self.get_field_square()
        finite_field = ['O']
        for i in range(0,self.P):
            if self.Curve.y_squared(i) % self.P in group_square.values():
                for key in group_square.keys():
                    if group_square[key] == self.Curve.y_squared(i) % self.P:
                        finite_field.append((i,key))

        return finite_field
    
    def add_points(self, pos1, pos2):
        finite_field = self.get_finite_field()
        value1, value2 = finite_field[pos1], finite_field[pos2]

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

curve_fields_to_generate = [(3,2,7),(2,7,11),(4,5,11)]

def prob_5_5():
    for cf in curve_fields_to_generate:
        cfg = EllipticCurveField( cf[0], cf[1], cf[2] )
        print(cfg.get_finite_field())

def prob_5_6():
    curve_field = EllipticCurveField(2,3,7)
    curve_field.get_addition_table()

def tester():
    cf = EllipticCurveField(3, 8, 13)
    cf.get_addition_table()

def prob_5_7():
    cfb = EllipticCurveField(1,1,5)
    print(cfb.get_finite_field())

    cfc = EllipticCurveField(1,1,7)
    print(cfc.get_finite_field())

prob_5_7()