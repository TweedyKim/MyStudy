fruits = ['오렌지' , '사과', ' 바나나']
price = [300, 400, 500]
print("{} {} {}".format(fruits[0], fruits[0:2], fruits[-1]))

x = [fruits, price]
print(x[0][1], " " , len(x))

y = fruits + price
print(y[5], " ", len(y))

fruits.append('체리')
print(fruits)

fruits.extend(['딸기', '복숭아'])
print(fruits, " ", len(fruits))

fruits.insert(2, '포도')
print(fruits, " ", len(fruits))
print(fruits.pop(4))

del fruits[2]
print(fruits, " ", len(fruits))

fruits.remove('딸기')
print(fruits, " ", len(fruits))

print('사과' in fruits)

fruits.clear()
print(fruits, " ", len(fruits))
