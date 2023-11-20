f = open('challenge4.txt', 'r')
hexStringPool = f.readlines() #读取字符串
candidate = [] #存放对于每个字符串来说单字符异或加密得分最高的结果
for line in hexStringPool:
    line = line.strip() #移除字符串头尾的空格或换行符
    string = line.decode('hex') #16进制解码
    #对每个字符串调用traversal_singlebyte方法，将得分最高的存放在candidate列表中
    candidate.append(traversal_singlebyte(string))

#返回列表中得分最高的一项的解密结果，即为所要寻找的字符串解密结果。
print sorted(candidate, key = lambda c:c['score'])[-1]['plaintext']
