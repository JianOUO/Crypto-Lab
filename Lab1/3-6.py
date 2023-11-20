import itertools
import base64

def hamming_distance(s1, s2):
    dis = 0
    for i in range(min(len(s1), len(s2))):
        b = bin(ord(s1[i]) ^ ord(s2[i]))
        dis += b.count('1')
        return dis
def guess_keysize(string):
    keys = []
    for keysize in range(2, 40):
        blocks = []
        count = 0
        dis = 0
        for i in range(0, len(string), keysize):
            count += 1
            blocks.append(string[i:i+keysize])
            if count == 4:
                break
        #选取四个块，两两组合求汉明距离
        pairs = itertools.combinations(blocks, 2)
        for (x, y) in pairs:
                dis += hamming_distance(x, y)
        ndis = dis / keysize
        key = {'keysize': keysize, 'distance': ndis}
        keys.append(key)
    return sorted(keys, key=lambda c:c['distance'])[0:3]

def guess_key(keysize, string):
    key = ''
    for i in range(keysize):
        now_str = ''
        #获取每个块相同位置的字符
        for index, ch in enumerate(string):
            if index % keysize == i:
                now_str += ch
                key += chr(traversal_singlebyte(now_str)['key'])
        return key

def break_repeatingkey_xor(string):
    keysizes = guess_keysize(string)
    candidate = []
    plains = []
    for keysize in keysizes:
        key = guess_key(keysize['keysize'], string)
        #二元组：重复密钥异或解密明文，对应密钥key
        plains.append((hex_to_str(repeatingkey_xor(string, key)), key))
        return sorted(plains, key=lambda c:get_score(c[0]))[-1]

f = open('challenge6.txt', 'r')
s = f.read() string=base64.b64decode(s)
res=break_repeatingkey_xor(string)
print 'plaintext: \n'+res[0]
print 'key: \n'+res[1]
