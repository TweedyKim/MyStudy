#Built-in Function

print('===================================================================')
print('|  Built-in Function #1                                           |')
print('|  1.callable                                                     |')
print('|    -> Return a boolean whether a function or a method can       |')
print('|       call or can not call.                                     |') 
print('|  2.@property                                                    |')
print('|    -> transfer attribution from method to property.             |')
print('|  4.@staticmethod                                                |')
print('|    -> It makes for instance to call staticmethod.               |')
print('|  4.hasattr                                                      |')
print('|    -> Return a boolean whether an object exist or not.          |')
print('|  5.getattr                                                      |')
print('|    -> Get an attribute of an existing object.                   |')
print('|  6.hash                                                         |')
print('|  7.id                                                           |')
print('|-----------------------------------------------------------------|')
print('|  TestCls is a Class.                                            |')
print('|   1. Property                                                   |')
print('|      1) TsProperty                                              |')
print('|   2. Method                                                     |')
print('|      1) Static_method_1 -> use @staticmethod                    |')
print('|      2) Static_method_2                                         |')
print('|      3) TsMethod_1                                              |')
print('|      4) TsMethod_2 -> use @property                             |')
print('|      5) TsMethod_3                                              |')
print('|   4.TestIns_1 is a instance which comes from TestCls.           |')
print('|-----------------------------------------------------------------|')
print('|  ChildCls is a Class which is inherited from "TestCls".         |')
print('|   1. Method                                                     |')
print('|      1) TsMethod_1                                              |')
print('|-----------------------------------------------------------------|')
print('|  Remark                                                         |')
print('|   1. self: When it makes instance, all methods which have       |')
print('|            "self" argument are referenced in memory.            |')
print('|   2. super: It points a parents class                           |')
print("===================================================================\n\n")


class TestCls:
    TsProperty = "Class Property"
    ClsName_1 = ''
    
    def __init__(self, ClsName):
        self.ClsName_1 = ClsName

    @staticmethod
    def Static_method_1():
        print('Static_method_1 in TestCls is called.')
        print('This is none-return type.')

    def Static_method_2():
        print('Static_method_2 in TestCls is called.')

    def TsMethod_1(self):
        print('TsMethod_1 in {} is called.'.format(self.ClsName_1))
        return 'End TsMethod_1 in ' + self.ClsName_1

    @property
    def TsMethod_2(self):
        #print('\n"TsMethod_2" in TestCls is called.')
        #print('This is none-return type.\n')
        return 'TsMethod_2 in {} is called.'.format(self.ClsName_1)

    def TsMethod_3(self):
        print('TsProperty in this instance is', self.TsProperty)
        return 'End TsMethod_3 in ' + self.ClsName_1

class ChildCls(TestCls):
    ClsName = ""

    def __init__(self, ClsName):
        super().__init__("parents class")
        self.ClsName = ClsName
        print('Initialize {} with its parents class.'.format(self.ClsName))
    
    def TsMethod_1(self):
        print('The result of "super().TsMethod_1" is')
        a = super().TsMethod_1()
        print(a)
        return 'End TsMethod_1 in ' + self.ClsName
    

TestIns_1 = TestCls("TestIns_1")

print('1. callable')
rslt_1 = callable(TestCls.Static_method_1)
rslt_2 = callable(TestCls.Static_method_2)

rslt_3 = callable(TestCls.TsMethod_1)
rslt_4 = callable(TestCls.TsMethod_2)
rslt_5 = callable(TestCls.TsMethod_3)

rslt_6 = callable(TestIns_1.TsMethod_1)
#rslt_7 = callable(TestIns_1.TsMethod_2)
rslt_8 = callable(TestIns_1.TsMethod_3)

print('   The result of "callable(TestCls.Static_method_1)" is', rslt_1)
print('   The result of "callable(TestCls.Static_method_2)" is', rslt_2)

print('   The result of "callable(TestCls.TsMethod_1)" is', rslt_3)
print('   The result of "callable(TestCls.TsMethod_2)" is', rslt_4)
print('   The result of "callable(TestCls.TsMethod_3)" is', rslt_5)

print('   The result of "callable(TestIns_1.TsMethod_1)" is', rslt_6)
#print('The result of "callable(TestIns_1.TsMethod_2)" is', rslt_7)
print('   The result of "callable(TestIns_1.TsMethod_3)" is', rslt_8)
print("\n")

print('2. @property')
print('   The result of "TestIns_1.TsMethod_2" \n ->', TestIns_1.TsMethod_2)
print("\n")

print('3. @staticmethod')
print('   The result of "TestIns_1.Static_method_1()" \n')
TestIns_1.Static_method_1()
print("\n")

print('4. hasattr')
print('   Existing "get_name" attributie in TestIns_1 is', hasattr(TestIns_1, 'get_name'))
print('   Existing "TsMethod_1" attributie in TestIns_1 is', hasattr(TestIns_1, 'TsMethod_1'))
print("\n")

print('5. getattr')
print('   The result of "getattr(TestIns_1, {})()" is'.format("'TsMethod_1'"))
print(getattr(TestIns_1, 'TsMethod_1')())
print("\n")

print('6. hash & id')
print("   TsIns_1's hash: {}  id: {}".format(hash(TestIns_1), id(TestIns_1)))
#isinstance(), issubclass()
print("\n")

TestIns_2 = ChildCls('TestIns_2')
print("\n")

print('. Super')
print(TestIns_2.TsMethod_1())






