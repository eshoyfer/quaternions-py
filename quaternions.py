import math

# Python Quaternion class
# By eshoyfer

class Quaternion:
    EPSILON = 10 ** -10

    # Init with 4 component arguments
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    # Overloading string operator
    def __str__(self):
        return str(self.a) + " + " + str(self.b) + "i + " + str(self.c) + "j + " + str(self.d) + "k"

    # Overloading addition operator Q1 + Q2
    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    # Overloading multiplication operator
    # Q1 * Q2
    '''
    (Q1 * Q2).w = (w1w2 - x1x2 - y1y2 - z1z2)
    (Q1 * Q2).x = (w1x2 + x1w2 + y1z2 - z1y2)
    (Q1 * Q2).y = (w1y2 - x1z2 + y1w2 + z1x2)
    (Q1 * Q2).z = (w1z2 + x1y2 - y1x2 + z1w2)
    '''
    def __mul__(self, other):
        m1 = (self.a * other.a) - (self.b * other.b) - (self.c * other.c) - (self.d * other.d)
        m2 = (self.a * other.b) + (self.b * other.a) + (self.c * other.d) - (self.d * other.c)
        m3 = (self.a * other.c) - (self.b * other.d) + (self.c * other.a) + (self.d * other.b)
        m4 = (self.a * other.d) + (self.b * other.c) - (self.c * other.b) + (self.d * other.a)
        return Quaternion(m1, m2, m3, m4)

    # Overloading pow (**) operator: Q ** n
    def __pow__(self, n):
        pow = Quaternion(1, 0, 0, 0) # Identity aka Quaternion.ONE
        for i in range(n):
            pow = pow * self
        return pow

    def __eq__(self, other):
        a_close = abs(self.a - other.a) < self.EPSILON
        b_close = abs(self.b - other.b) < self.EPSILON
        c_close = abs(self.c - other.c) < self.EPSILON
        d_close = abs(self.d - other.d) < self.EPSILON
        return a_close and b_close and c_close and d_close

    # Scalar multiplication
    # Future: might be more pleasant to overload __mul__
    def scale(self, k):
        return Quaternion(self.a * k, self.b * k, self.c * k, self.d * k)

    def norm(self):
        return (self.a**2 + self.b**2 + self.c**2 + self.d**2) ** 0.5

    def normalized(self):
        N = self.norm()
        return Quaternion(self.a / N, self.b / N, self.c / N, self.d / N)

    def conj(self):
        return Quaternion(self.a, self.b * -1, self.c * -1, self.d * -1)

    def is_unit(self):
        return abs(self.norm() - 1) < self.EPSILON

    def scalar(self):
        return self.a

    def vector(self):
        return [self.b, self.c, self.d]

    def components(self):
        return self.a, self.b, self.c, self.d

# Class static constant instances
# For bases export
Quaternion.ONE = Quaternion(1, 0, 0, 0)
Quaternion.I = Quaternion(0, 1, 0, 0)
Quaternion.J = Quaternion(0, 0, 1, 0)
Quaternion.K = Quaternion(0, 0, 0, 1)

q1 = Quaternion(1, 0, 1, 0)
q2 = Quaternion(1, 0.5, 0.5, 0.75)
q3 = Quaternion(1, 0, 1, 0)

print "*** TESTS ***"

print "Q1:", q1, "|", "Q2:", q2
print "Quaternion Addition:", q1 + q2
print "Quaternion Multiplication:", q1 * q2
print "Scalar Multiplication:", q1.scale(5)
print "Quaternion Exponentiation:"
for i in range(5):
    print q1 ** i, "| Exponent =", i
print "Quaternion Norm", q1.norm()
print "Quaternion Normalization:", "The magnitude of", q1.normalized(), "is", q1.normalized().norm()
print "Quaternion Unit Check:", q1, "Unit?", q1.is_unit(), "|", q1.normalized(), "Unit?", q1.normalized().is_unit()
print "The conjugate of", q1, "is", q1.conj()
print "Q1 == Q2?", q1 == q2, "|", "Q1 == Q3?", q1 == q3
print Quaternion.ONE, Quaternion.I, Quaternion.J, Quaternion.K
print "ij", Quaternion.I * Quaternion.J
print "jk", Quaternion.J * Quaternion.K
print "ki", Quaternion.K * Quaternion.I
print "i**2 == j**2 == k**2 == ijk == -1?"
print "i**2", Quaternion.I ** 2
print "j**2", Quaternion.J ** 2
print "k**2", Quaternion.K ** 2
print "ijk", Quaternion.I * Quaternion.J * Quaternion.K




