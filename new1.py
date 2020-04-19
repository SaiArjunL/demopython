class operator:
    def __init__(ob1,m1,m2):
        ob1.m1 = m1
        ob1.m2 = m2

    def __add__(ob2, other):
        m1 = ob2.m1 + other.m1
        m2 = ob2.m2 + other.m2
        s3 = operator(m1,m2)
        return s3

    def __mul__(ob3, other):
        m1 = ob3.m1 * other.m1
        m2 = ob3.m2 * other.m2
        s3 = operator(m1,m2)
        return s3

a = operator(90,85)
b = operator(80,85)
c = a + b
d = a * b
print(c.m1)
print(c.m2)
print(d.m1)
print(d.m2)
