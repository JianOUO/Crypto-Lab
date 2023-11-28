from Crypto.Util.number import getPrime

def invmod(a, n):
    b, c = 1, 0
    while n:
        q, r = divmod(a, n)
        a, b, c, n = n, c, b - q*c, r
    # 此时a是原始输入的最大公约数
    if a == 1:
        return b
    raise ValueError("Not invertible")

class RSA:
    def __init__(self, key_len: int = 100):
        # 密钥生成
        while True:
            # 重复直到找到与e互质的et
            try:
                # 生成2个随机素数
                p, q = getPrime(key_len), getPrime(key_len)

                # RSA运算是模n运算
                n = p * q

                # 计算"欧拉函数"
                et = (p - 1) * (q - 1)
                e = 3

                # 计算私钥
                d = invmod(e, et)
                break

            except ValueError:
                continue

        # 密钥摘要
        self.n = n
        self.d = d
        self.e = e

    def encrypt(self, m: bytes) -> int:
        m = self.bytes_to_num(m)
        c = pow(m, self.e, self.n)
        return c

    def decrypt(self, c: int) -> bytes:
        m = pow(c, self.d, self.n)
        m = self.num_to_bytes(m)
        return m

    @staticmethod
    def bytes_to_num(seq: bytes) -> int:
        return int(seq.hex(), 16)

    @staticmethod
    def num_to_bytes(seq: int) -> bytes:
        hex_rep = hex(seq)[2:]
        hex_rep = '0' * (len(hex_rep) % 2) + hex_rep
        return bytes.fromhex(hex_rep)


def main():
    rsa_obj = RSA(key_len=1024)
    m = b'RSA implementation'
    c = rsa_obj.encrypt(m)
    print(f'{c=}')

    m_rec = rsa_obj.decrypt(c)
    print(f'{m_rec=}')


if __name__ == '__main__':
    main()


