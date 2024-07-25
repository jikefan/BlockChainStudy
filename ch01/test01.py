from random import randint
from helper import hash256
from ecc import N, PrivateKey, S256Point


if __name__ == "__main__":
    G = S256Point(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    
    z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
    r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
    s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
    
    px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
    py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
    point = S256Point(px, py)
    
    s_inv = pow(s, N - 2, N)
    u = z * s_inv % N
    v = r * s_inv % N
    
    print((u*G + v*point).x.num == r)
    
    print('签名测试')
    
    pk = PrivateKey(randint(0, N))
    z = randint(0, 2**256)
    sig = pk.sign(z)
    result = pk.point.verify(z, sig)
    print(result)