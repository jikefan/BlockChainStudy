from helper import hash256
from ecc import N, FieldElement, Point, S256Point

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
    