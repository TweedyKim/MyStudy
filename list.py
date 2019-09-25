#List
fruits = ['오렌지', '사과', '바나나']
price = [100, 200, 300]
things = ['ok', 'no']
print(fruits[0], fruits[0:2], fruits[-1])

new_2nd_arr = [fruits, price]
new_1st_arr = fruits + price
print(new_2nd_arr, " ",  len(new_2nd_arr))
print(new_1st_arr, " ", len(new_1st_arr))

price.append(400)
print(price)
price.extend(things)
print(price)
price.insert(4, 500)
print(price)
print(price.pop(4))     #pop은 return 값이 있음, Del은 없음
print(price)
price.remove('ok')
print(price)
del price[len(price)-1]
print(price)
price.extend(things)
print('ok' in price)
print(price)
del price[1:1]  #?
print(price)
price.clear()
print(price)



