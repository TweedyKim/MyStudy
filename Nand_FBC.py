
global iCol_Size
global iCol_Spare_Size
global iCol_Tot_Size


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
            

def GetBlkNo(strX_add):
    iBlk_Cnt = 64
    iX_add = Conv_Hex_To_Int(strX_add)
    return divmod(iX_add,iBlk_Cnt)

def GetECCBlkNo(strY_add):
    iY_add = Conv_Hex_To_Int(strY_add)
    iMECC_Size = iCol_Size / 4
    iSECC_Size = iCol_Spare_Size / 4
    if iY_add < iCol_Size:
        return int(iY_add / iMECC_Size)
    else:
        iY_add -= iCol_Size
        return int(iY_add / iSECC_Size) + 4

iCol_Size = int(input ("Input the size of column\n =>"))
iCol_Spare_Size = int(input ("Input the size of column spare\n =>"))
iCol_Tot_Size = iCol_Size + iCol_Spare_Size
print('1. Column Size       :', iCol_Size)
print('2. Column Spare Size :', iCol_Spare_Size)
print('3. Column Total Size :', iCol_Tot_Size)

iSeq_Xadd = 1
iSeq_Yadd = 0
iSeq_Blk = 0
iSeq_Page = 1

dicFail_Info = {}

with open('D:\dut33_108c.asc', mode= 'rt', encoding='utf-8') as fr:
    bFlag = False
    for line in fr:
        line = line.strip()
        if len(line) != 0:
            if line.find('BIT #') >= 0 and line.find('OUTPUT') >= 0:
                bFlag = False
            if bFlag == True:
                lstAddress = line.replace('#','').split('  ')
                del lstAddress[0]
                lstAddress[0] = lstAddress[0].strip()
                for fadd in lstAddress:
                    tpBlk_Page_No = GetBlkNo(fadd.split(' ')[iSeq_Xadd])
                    iECC_Blk_No = GetECCBlkNo(fadd.split(' ')[iSeq_Yadd])
                    keyECC_Blk =  '%d_%d_%d' % (tpBlk_Page_No[iSeq_Blk], tpBlk_Page_No[iSeq_Page], iECC_Blk_No)
                    #================================================================================
                    #iFail_Cnt[[tpBlk_Page_No[iSeq_Blk]][[tpBlk_Page_No[iSeq_Page]][[iECC_Blk_No]] += 1
                    #================================================================================
                    
                    if keyECC_Blk in dicFail_Info:
                        dicFail_Info[keyECC_Blk][0] += 1
                        dicFail_Info[keyECC_Blk].append(fadd)
                    else:
                        dicFail_Info[keyECC_Blk] = [1, fadd]
            if line.find('F-CNT') >=0:
                bFlag = True

with open('D:\dut33_108c_summary.csv', mode= 'wt', encoding='utf-8') as fw:
    for key, val in dicFail_Info.items():
        Blk = str(key).split('_')
        fw.write('Blk%03d,Page%02d,ECC%d,%02d,' % (int(Blk[0]), int(Blk[1]), int(Blk[2]), val[0]))
        for i in range(1,len(val)):
            fw.write('(Y{} X{}),'.format(str(val[i]).split(' ')[0] , str(val[i]).split(' ')[1]))

        fw.write('\n')
