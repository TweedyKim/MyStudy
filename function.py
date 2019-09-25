lst = ["오렌지", "사과", "배"]
dic = {'오렌지':400, '사과':200, '배':100}

for key in dic:
    print("key=", key, dic[key])

print(list(enumerate(lst)))

for i, value in enumerate(lst):
    print("tt",i,value)
    print(lst[i])

for i in lst:
    print(i)

for key, element in dic.items():
    print("items.key=", key, ", element=", element)

for i in range(0,11,2):
    print(i)

arr = [i **2 for i in range(0, 20, 2)]
print(arr)
print("min={} max={}".format(min(arr), max(arr)))

x=[]
for i in range(0,20,2):
    x.append(i ** 2)
    if i == 18:
        print(x)

outs=[f for f in lst if f != '사과']
print(outs)

