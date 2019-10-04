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
print('print fruits[0] is', fruits[0])
print('print fruits[0:2] is', fruits[0:2])
print('print fruits[-1] is', fruits[-1])
print('\n')

print('2. list unify')
print('the result of "[fruits, num]" is', [fruits, num])
print('the result of "fruits + num" is', fruits + num)
print('\n')

print('4. append, extend & insert')
num.append(400)
print('execute "num.append(400)" and print num is', num)
num.extend(reply)
print('execute "num.extend(reply)" and print num is', num)
num.insert(4, 500)
print('execute "num.insert(4, 500)" and print num is', num)
print('\n')

print('5. pop, revmoe & del')
print('print "num.pop(4)" is', num.pop(4))
print('print num is', num, ' => "500" has been deleted because of pop function')
num.remove('ok')
print('execute "num.remove("ok")" and print num is', num)
del num[len(num)-1]
print('execute "del price[len(price)-1]" and print num is', num)
print('#Remark: Difference of pop & del')
print('         pop is fucntion. Therefore it has argument & return value')
print('         del is attribution. Therefore is has no return value')
print('\n')

print('6. extend & clear')
num.extend(reply)
print('execute "num.extend(reply)" and print num is', num)
print('search "ok" in num and result is', 'ok' in num, ' =>["ok" in num]') 
#del price[1:1]  #?
#print(price)
num.clear()
print('execute "num.clear()" and print num is', num)



