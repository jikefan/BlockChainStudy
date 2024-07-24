from chapter01 import FieldElement


class Point:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if self.x == None and self.y == None:
            return
        if self.y ** 2 != self.x ** 3 + a * self.x + b:
            raise ValueError("Point({}, {}) is not on the curve".format(x, y))
        
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b
    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise ValueError("Points {} and {} are not on the same curve".format(self, other))
        
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)
        
        if self.x == None and self.y == None:
            return other
        if other.x == None and other.y == None:
            return self
        
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            
            x3 = s ** 2 - other.x - self.x
            
            y3 = s * (self.x - x3) - self.y
            return self.__class__(x3, y3, self.a, self.b)
        
        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
    
    def __repr__(self) -> str:
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)
    
    def __rmul__(self, coefficient):
        # product = self._ _class_ _(None, None, self.a, self.b)
        # for _ in range(coefficient):
        #     product += self
        # return product
        
        # 二进制展开加速计算
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result
    
P = 2**256 - 2**32 - 977
class S256Field(FieldElement):
    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=P)
    
    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(S256Field(x), S256Field(y), a, b)
        else:
            super().__init__(x, y, a, b)
            
    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)

    def __repr__(self):
        if self.x is None:
            return 'S256Point(infinity)'
        else:
            return 'S256Point({},{})'.format(self.x, self.y)


if __name__ == "__main__":
    prime = 223
    a = FieldElement(num=0, prime=prime)
    b = FieldElement(num=7, prime=prime)
    x1 = FieldElement(num=192, prime=prime)
    y1 = FieldElement(num=105, prime=prime)
    x2 = FieldElement(num=17, prime=prime)
    y2 = FieldElement(num=56, prime=prime)
    p1 = Point(x1, y1, a, b)
    p2 = Point(x2, y2, a, b)
    print(p1+p2)
    
    print(2 * p1)
    
    gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    
    p = 2**256 - 2**32 - 977
    print(gy**2 % p == (gx**3 + 7) % p)
    
    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    
    x = FieldElement(num=gx, prime=p)
    y = FieldElement(num=gy, prime=p)
    seven = FieldElement(num=7, prime=p)
    zero = FieldElement(num=0, prime=p)
    G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    print(N*G)
    