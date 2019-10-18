#List

fruits = ['오렌지', '사과', '바나나', '배']
num = [100, 200, 300]
reply = ['ok', 'no']

print('=========================[List]=========================')
print('fruits is', fruits)
print('price is', num)
print('things is', reply)
print('\n')

print('1. serval ways to print items in list')
print('   print fruits[0] is', fruits[0])
print('   print fruits[0:2] is', fruits[0:2])
print('   print fruits[-1] is', fruits[-1])
print('\n')

print('2. list unify')
print('   the result of "[fruits, num]" is', [fruits, num])
print('   the result of "fruits + num" is', fruits + num)
print('\n')

print('4. append, extend & insert')
num.append(400)
print('   execute "num.append(400)" and print num is', num)
num.extend(reply)
print('   execute "num.extend(reply)" and print num is', num)
num.insert(4, 500)
print('   execute "num.insert(4, 500)" and print num is', num)
print('\n')

print('5. pop, revmoe & del')
print('   print "num.pop(4)" is', num.pop(4))
print('   print num is', num, ' => "500" has been deleted because of pop function')
num.remove('ok')
print('   execute "num.remove("ok")" and print num is', num)
del num[len(num)-1]
print('   execute "del price[len(price)-1]" and print num is', num)
print('   #Remark: Difference of pop & del')
print('            pop is fucntion. Therefore it has argument & return value')
print('            del is attribution. Therefore is has no return value')
print('\n')

print('6. extend & clear')
num.extend(reply)
print('   execute "num.extend(reply)" and print num is', num)
print('   search "ok" in num and result is', 'ok' in num, ' =>["ok" in num]') 
#del price[1:1]  #?
#print(price)
num.clear()
print('   execute "num.clear()" and print num is', num)
print('\n')

print('7. Definition of list')
b = list()
c = []
print('   The result of "b = list[]" is', b)
print('   The result of "c = []" is', c)

print("8. iterable functions - list, Join & tuple")
iNum = '12345678'
cStr = '김동훈천재'
iLst = list(iNum)
cLst = list(cStr)
iJoin = '.'.join(iLst)
cJoin = '-'.join(cLst)
iTuple = tuple(iLst)
cTuple = tuple(cLst)
print('   iNmu is "%s"' % iNum, ' and the type of iNum is', type(iNum))
print('   cStr is "%s"' % cStr, ' and the type of cStr is', type(cStr))

print('   iLst is the result of "list(iNum)". ->', iLst, ' and the type of iLst is', type(iLst))
print('   cLst is the result of "list(cStr)". ->', cLst, ' and the type of cLst is', type(cLst))

print('   iJoin is the result of "join(iLst)". ->', iJoin, ' and the type of iJoin is', type(iJoin))
print('   cJoin is the result of "join(cLst)". ->', cJoin, ' and the type of cJoin is', type(cJoin))

print('   iTuple is the result of "tuple(iLst)". ->', iTuple, ' and the type of iJoin is', type(iTuple))
print('   cTuple is the result of "tuple(cLst)". ->', cTuple, ' and the type of cJoin is', type(cTuple))

print("\n")


#=============================================================================
#다차원 동적 배열 방법
lstFail_Cnt = [[[0] * 8 for i in range(0,64)] for j in range(0,3)]
lstBuf = [[[1] * 8 for i in range(0,64)]]
lstFail_Cnt.append(lstBuf)
#=============================================================================

