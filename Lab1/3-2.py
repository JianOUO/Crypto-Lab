def xor(b1, b2):
    res = []
    for i in range(len(b1)):
        res.append(b1[i] ^ b2[i])
    return res

def bytelist_to_hex(byteList):
    return "".join(hex(x)[2:] if x > 15 else '0' + hex(x)[2:] for x in byteList)

def hex_to_bytelist(hexString):
    return [ord(c) for c in hexString.decode("hex")]

def fixed_xor(s1, s2):
    return bytelist_to_hex(xor(hex_to_bytelist(s1), hex_to_bytelist(s2)))

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
print fixed_xor(s1, s2)