#Tuple(Read Only List) => Paster then List

print("Tuple(Read Only List) : faster then List\n")
print('=========================[Tuple]=========================')
fruits = ('오렌지', '사과', '바나나')
print('fruits is', fruits)

print("1. print each item in tuple")
print("print fruits[0] is",fruits[0])
print("print fruits[1] is",fruits[1])
print("\n")

print("2. transfer from varialbe to tuple")
x, y = 1, 2
print("print x is" ,x)
print("print y is" ,y)
(x, y)
print("The result of (x, y) is",x,y)
print("\n")

print("3. transfer from list to tuple")
things = ['a', 'b', 'c']
print("print things is", things, "\n things is list")
q = things[0], things[1]        #List에서 특정 값을 가져오면 Tuple이 된다. Return 시 Tuple임
print("The result of q = things[0], things[1] is", q)
print("\n")
