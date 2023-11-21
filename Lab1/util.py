def hex_to_bytelist(hexString): 
    return [ord(c) for c in hexString.decode("hex")]

def bytelist_to_hex(byteList): 
    return "".join(hex(x)[2:] if x > 15 else '0' + hex(x)[2:] for x in byteList)

def str_to_bytelist(string):
    return hex_to_bytelist(str_to_hex(string))

def str_to_hex(string):
    return string.encode("hex")

def hex_to_str(hexString): 
    return hexString.decode("hex")

def bytelist_to_str(byteList): 
    return hex_to_str(bytelist_to_hex(byteList))

def xor(b1, b2): 
    res = [] 
    for i in range(len(b1)): 
        res.append(b1[i] ^ b2[i]) 
    return res
