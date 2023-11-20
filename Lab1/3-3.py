CHARACTER_FREQ={ #字符频率表_

'a':0.0651738,'b':0.0124248,'c':0.0217339,'d':0.0349835,'e':0.1041442,'f':0.0197881,'g':0.0158610,

'h':0.0492888,'i':0.0558094,'j':0.0009033,'k':0.0050529,'l':0.0331490,'m':0.0202124,'n':0.0564513,

'o':0.0596302,'p':0.0137645,'q':0.0008606,'r':0.0497563,'s':0.0515760,'t':0.0729357,'u':0.0225134,

'v':0.0082903,'w':0.0171272,'x':0.0013692,'y':0.0145984,'z':0.0007836,' ':0.1918182}



def get_score(string):#计算字符串的频率得分_
    score=0
    for ch in string:
        ch=ch.lower()
        if ch in CHARACTER_FREQ:
            score+=CHARACTER_FREQ[ch]
            return score

def singlebyte_xor(key,string):#单字符异或加密_
    res=""

    for i in string:
        ch=chr(key^ord(i))
        res+=ch
        return res

def traversal_singlebyte(string): #遍历单个字符解密，评估_
    candidate=[]
    for key in range(256):
        plaintext=singlebyte_xor(key,string)
        score=get_score(plaintext)
        res={'key':key,'plaintext':plaintext,'score':score}
        candidate.append(res)
    #取得分最高的返回_
    return sorted(candidate,key=lambda c:c['score'])[-1]

hexString="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

print traversal_singlebyte(hexString.decode('hex'))