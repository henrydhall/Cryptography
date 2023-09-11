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
    
    def get_addition_table(self):
        finite_field = self.get_finite_field()
        print('         ' + str(finite_field))
        for row in finite_field:
            print(str(row).rjust(6))
        # TODO: addition algorithm...
        # TODO

curve_fields_to_generate = [(3,2,7),(2,7,11),(4,5,11)]

def prob_5_5():
    for cf in curve_fields_to_generate:
        cfg = EllipticCurveField( cf[0], cf[1], cf[2] )
        print(cfg.get_finite_field())

def prob_5_6():
    curve_field = EllipticCurveField(2,3,7)
    curve_field.get_addition_table()

prob_5_6()