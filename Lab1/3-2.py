import util
def fixed_xor(s1, s2):
    return util.bytelist_to_hex(util.xor(util.hex_to_bytelist(s1), util.hex_to_bytelist(s2)))

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
print fixed_xor(s1, s2)
