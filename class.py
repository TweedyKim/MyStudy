class Dog: 
    #self: instance 생성 시 자기 자신을 의미
    def __init__(self,name):
        self.name = name
        print(self.name, " was born")
    
    def speak(self):
        print("YELP!", self.name)
    
    def wag(self):
        print("Dog's wag tail")

    def __del__(self):
        print("destroy!!")
    
class Puppy(Dog):
    def __init__(self):
        self.name = "Puppy"

    #capsulation
    def __read_diary(self):
        print("My screte")

    def speak(self):
        print("Bow wow", self.name)
    
    def wag(self):
        self.__read_diary()
        print("Puppy's wag tail")
    
    #Static Method on Class
    def scm():
        print("Duke~~~!!")

class Test:
    def __init__(self):
        print("Test init")

    def test(self):
        print("Test Class")
        self.__q()
    
    def __q(self):
        print("Call capsulation function")  

#Method는 상속하는 Class보다 상속받는 Class가 우선 순위를 갖는다.
d = Dog("Shit")
p = Puppy()

p.wag()
#Call Static Method on Class
Puppy.scm()

ta = Test()
ta.test()
print("end")