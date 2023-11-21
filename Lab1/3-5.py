import util
def repeatingkey_xor(string, key):
    res="" #字符串连接，存放每一次加密后的结果
    #xrange方法使得每次处理len(key)长度的字符串
    for i in xrange(0, len(string), len(key)):
        res += util.bytelist_to_hex(util.xor(util.str_to_bytelist(string[i:i+len(key)]), util.str_to_bytelist(key)))
        return res
string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
print repeatingkey_xor(string, key)
