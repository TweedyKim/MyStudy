#Tuple(Read Only List) => Paster then List
fruits = ('오렌지', '사과', '바나나')
print(fruits[0], fruits[1])

x, y = 1, 2
print(x,y)
(x, y)
print(x,y)

things = ['a', 'b', 'c']
q = things[0], things[1]        #List에서 특정 값을 가져오면 Tuple이 된다. Return 시 Tuple임
print(q)
