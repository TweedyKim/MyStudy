#Built-in Function

import random
import time

class TestClass:
    name = "TEST"

    @staticmethod
    def static_method():
        print("static_mothod on TestClass")

    def get_name(self):
        return "get name on test instance :" + self.name

    @property
    def full_name(self):
        return self.name + " property"

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("intance in child class Init")
    
    def get_name(self):
        super().get_name
        return "get_name print on TestClass :" + self.name
    

test = TestClass()
print(test.get_name())
c = callable(test.get_name)
print("callable print :", c)

child = Child()
child.get_name()

print("@staticmethod test :", test.static_method())
print("@property test :", test.full_name)

print("Check to exist attribute :", hasattr(test, 'get_name'))
print("getattr test")
getattr(test, 'get_name')()
print("getattr test")
getattr(TestClass, 'static_method')()

print("hash: {}  id: {}".format(hash(test), id(test)))
#isinstance(), issubclass()

print("")
print("")
print("abs(-10) :", abs(-10))                 #절대값
print("divmod(5,2) :", divmod(5,2))              #몫 & 나머지
print("bin(17) :", bin(17), "  bin(0o17) :", bin(0o17))       #2진수 변환
print("oct(17) :", oct(17))                  #8진수 변환
print("hex(0b1101) :", hex(0b1101))              #16진수 변환
print("bool(0) :", bool(0), "bool(3) :", bool(3), "bool("") :", bool(""))
print("pow(2,10) :", pow(2,10))

print("")
print("")
print("help(min)")
help(min)

print("")
print("")
print("type(10) :", type(10))
#range(1,20,2)
print("round(2.5), round(2.51) :", round(2.5), round(2.51))
print("round(3.5), round(3.51) :", round(3.5), round(3.51))
print("round(4.5), round(4.51) :", round(4.5), round(4.51))
print("round(1.5), round(2.5), round(2.51), round(2.3456,3), round(0.5)")
print(round(1.5), round(2.5), round(2.51), round(2.3456,3), round(0.5))
print("")
print("dir()")
print(dir())
print("")
print("dir(random)")
print(dir(random))
print("")
print("dir(time)")
print(dir(time))

print("")
print("")
print("eval & exec test : print('123')")
eval('print("123")')
exec('print("123")')

s ='김동훈'
print("s ='김동훈'")
print("len(s) =", len(s))

print("")
s1 = bytes(s, 'UTF8')
print("s1 = bytes(s, 'UTF8')")
print("s1 = ", s1)
print("len(s1) =", len(s1))
print("type(s1) =", type(s1))

print("")
s2 = bytearray(s, 'UTF8')
print("s2 = bytearray(s, 'UTF8')")
print("s2 =", s2)

print("")
s3 = bytearray(s, 'EUC-KR')
print("s3 = bytearray(s, 'EUC-KR')")
print("s3 =", s3)