import math

s = "123"
print("s = ", s)
print("list(s) = ", list(s))
print("join list(s)", "-".join(list(s)))
print("")

#file fucntion
#file = open(<file path>,<mode>)       => mode: w, a, r

#with는 자동으로 file session을 close 한다.
#with open(<file path>, "w") as file:
#   file.write("")

#with open(<file path>, "r") as file:
#   for line in file:
#       print(line)

print("iterable functions")
# list(), set(), tuple(), enumerate()
# min(), max(), sum(iter, start_value)

# import math => math.fsum(iter)
print("\n===============[sum]===============")
a = [2,3,5]
print("a =", a)
print("sum(a) =", sum(a))
print("sum(a,100) =", sum(a,100))
print("math.fsum(a) =", math.fsum(a))

# all(iter), any(iter)
print("\n============[all, any]=============")
a = [1,2,3,0]
print("a =", a)
print("all(a) =", all(a))
print("any(a) =", any(a))

#iter(), next() => iter는 data Return 후 delete한다.
print("\n===========[iter, next]============")
ai = iter(a)
print("ai :", ai)             # same with ai = next(iter(a))
print("next(ai, None) :", next(ai, None))
print("next(ai, None) :", next(ai, None))
print("next(ai, None) :", next(ai, None))
print("next(ai, None) :", next(ai, None))
print("next(ai, None) :", next(ai, None))

ai = iter(a)
print("ai :", ai)
print("next(ai, None) :", next(ai, None))
print("list(ai) :", list(ai))
print("next(ai, None) :", next(ai, None))

print("\n==============[zip]================")
a = [1,2,3]
b = [4,5,6]
d = [7,8]
c = zip(a,b)
e = zip(a,d)
print("a :",a)
print("b :", b)
print("d :", d)
print("c = zip(a,b) :", list(c))
print("e = zip(a,d) :", list(e))

# filter(filter_fn, iter) : filter object
print("\n============[filter]===============")
int_num = range(-5,6)
print(int_num)
print("list(int_num) :", list(int_num))
print("\nfilter negative value using by lambda")
negative = filter(lambda x: x<0, int_num)
print("negative = filter(lambda x: x<0, int_num) :", negative)
print("list(negative) :", list(negative))

print("\nfilter negative value using by function")
def fn(x): return x < 0
n2 = filter(fn, int_num)
print(list(n2))

print("\nfilter positive value using by lambda")
positive = filter(lambda x: x>=0, int_num)
print("positive = filter(lambda x: x>=0, int_num) :", positive)
print("list(positive) :", list(positive))


# map()
print("\n==============[map]================")
def fm(x): return x * 2
num = (1,2,3,4,5,6)
print("num :", list(num))
print("make double by using function")
dnum = map(fm, num)
print(list(dnum))
print("make triple by using lambda")
tri_num = map(lambda x: x * 3, num)
print(list(tri_num))
print("x < 3 by using lambda")
m = map(lambda x: x < 3, num)
print(list(m))


print("\n============[reduce]===============")
from functools import reduce
pro = 1
lst = [1,2,3,4]
print(list(lst))
for num in lst:
    pro = pro * num
print("all multiplex using by for :", pro)
pro2 = reduce(lambda x, y: x * y, lst)
print("all multiplex using by reduce :", pro2)