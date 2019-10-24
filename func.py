

def Conv_Hex_To_Int(strHex):
    strHex = list(strHex) ; strHex.reverse() ; strHex = ''.join(strHex)
    cnt = 0 ; iHex = 0
    for i in strHex:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            iHex += (ord(i) - ord('0')) * pow(16,cnt)
        elif ord(i) >= ord('A') and ord(i) <= ord('F'):
            iHex += (ord(i) - ord('A') + 10) * pow(16,cnt)
        cnt += 1
    return iHex