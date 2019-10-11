import random
import time


print('\n\n')
print('===================================================================')
print('|  Built-in Function #2                                           |')
print('|  1.math function                                                |')
print('|    1) abs    : absolute value                                   |')
print('|    2) divmod : remainder                                        |')
print('|    3) pow    : multiplier                                       |')
print('|    4) round  : rounding off to the nearest integer              |')
print('|  2.convert number                                               |')
print('|    -> transfer attribution from method to property.             |')
print('|  4.@staticmethod                                                |')
print('|    -> It makes for instance to call staticmethod.               |')
print('|  4.hasattr                                                      |')
print('|    -> Return a boolean whether an object exist or not.          |')
print('|  5.getattr                                                      |')
print('|    -> Get an attribute of an existing object.                   |')
print('|  6.hash                                                         |')
print('|  7.id                                                           |')
print("===================================================================\n\n")


print('1. Math Function - abs, divmod & round')
print('abs(-10) is', abs(-10))
print('divmod(5,2) is', divmod(5,2))
print('pow(2,10) is', pow(2,10))
print('round(0.5) is', round(0.5))
print('round(1.5) is', round(1.5))
print('round(2.5) is', round(2.5))
print('round(3.5) is', round(3.5))
print('round(4.5) is', round(4.5))
print('round(2.334456,3) is', round(2.334456,3))
print('\n')

print("bin(17) :", bin(17), "  bin(0o17) :", bin(0o17))       #2진수 변환
print("oct(17) :", oct(17))                  #8진수 변환
print("hex(0b1101) :", hex(0b1101))              #16진수 변환
print("bool(0) :", bool(0), "bool(3) :", bool(3), "bool("") :", bool(""))


print("\n\n")
print("help(min)")
help(min)

print("\n\n")
print("type(10) :", type(10))
#range(1,20,2)
#거리가 같다면 짝수를 선택함
print("\ndir()")
print(dir())
print("\ndir(random)")
print(dir(random))
print("\ndir(time)")
print(dir(time))

print("\n\n")
print("eval & exec test : print('123')")
eval('print("123")')
exec('print("123")')

s ='김동훈'
print("s ='김동훈'")
print("len(s) =", len(s))

print("\n")
s1 = bytes(s, 'UTF8')
print("s1 = bytes(s, 'UTF8')")
print("s1 = ", s1)
print("len(s1) =", len(s1))
print("type(s1) =", type(s1))

print("\n")
s2 = bytearray(s, 'UTF8')
print("s2 = bytearray(s, 'UTF8')")
print("s2 =", s2)

print("\n")
s3 = bytearray(s, 'EUC-KR')
print("s3 = bytearray(s, 'EUC-KR')")
print("s3 =", s3)