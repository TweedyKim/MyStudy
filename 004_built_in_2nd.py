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
print('|    1) bin  : convert a number to binary                         |')
print('|    2) oct  : convert a number to octa                           |')
print('|    3) hex  : convert a number to hex                            |')
print('|    4) bool : return a boolean value                             |')
print('|  3.help                                                         |')
print('|    -> It describes a function.                                  |')
print('|  4.dir                                                          |')
print('|    -> It shows functions in a library.                          |')
print('|  5.Fucntion for unicode                                         |')
print('|    1) bytes                                                     |')
print('|    2) bytearray                                                 |')
print('|  6.eval & exec                                                  |')
print("===================================================================\n\n")


print('1. Math Function - abs, divmod & round')
print('   abs(-10) is', abs(-10))
print('   divmod(5,2) is', divmod(5,2))
print('   pow(2,10) is', pow(2,10))
print('   round(0.5) is', round(0.5))
print('   round(1.5) is', round(1.5))
print('   round(2.5) is', round(2.5))
print('   round(3.5) is', round(3.5))
print('   round(4.5) is', round(4.5))
print('   round(2.334456,3) is', round(2.334456,3))
print('\n')

print('2. Convert number - bin, oct, hex & boolean')
print('   bin(17) is', bin(17), '\n   bin(0o17) is', bin(0o17))
print('   oct(17) is', oct(17), '\n   oct(0b01101) is', oct(0b01101))
print('   hex(0b1101) is', hex(0b1101), '\n   hex(255) is', hex(255))
print('   bool(0) is', bool(0), '\n   bool(3) is', bool(3), '\n   bool("") is', bool(""))
print('\n')


print('3. help')
print('decribe of "min" function')
help(min)
print('\n')

print('4. dir')
print('dir()\n', dir(),'\n')
print('dir(time)', dir(time))
print('\n')

print('5. Fucntion for unicode')
TsChr1 = 's'
TsChr2 = '김'
TsChr3 = bytes(TsChr1, 'UTF8')
TsChr4 = bytes(TsChr2, 'UTF8')
TsChr5 = bytearray(TsChr2, 'UTF8')
TsChr6 = bytearray(TsChr2, 'EUC-KR')

print('   TsChr1 is', TsChr1)
print('   The length of TsChr1 is', len(TsChr1))
print('   The type of TsChr1 is', type(TsChr1), '\n')

print('   TsChr2 is', TsChr2)
print('   The length of TsChr2 is', len(TsChr2))
print('   The type of TsChr2 is', type(TsChr2), '\n')

print('   TsChr3 is bytes(TsChr1, UTF8) =>', TsChr3)
print('   The length of TsChr3 is', len(TsChr3))
print('   The type of TsChr3 is', type(TsChr3), '\n')

print('   TsChr4 is bytes(TsChr2, UTF8) =>', TsChr4)
print('   The length of TsChr4 is', len(TsChr4))
print('   The type of TsChr4 is', type(TsChr4), '\n')

print('   TsChr5 is bytearray(TsChr2, UTF8) =>', TsChr5)
print('   The length of TsChr5 is', len(TsChr5))
print('   The type of TsChr5 is', type(TsChr5), '\n')

print('   TsChr4 is TsChr6 = bytearray(TsChr2, EUC-KR) =>', TsChr6)
print('   The length of TsChr6 is', len(TsChr6))
print('   The type of TsChr6 is', type(TsChr6), '\n')

print('6. eval & exec')
print("   eval & exec test : print('123')")
eval('print("   eval->123")')
exec('print("   exec->123")')
print("\n")

