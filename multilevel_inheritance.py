#Multilevel Inheritance

class A:
    x = 0
    y = 0

    def getA(self):
        self.x = 2
        self.y = 3


class B(A):
    w= 0
    v = 0
    z = 0
    def getB(self):
        self.z = self.x+self.y
        print("Addition",self.z)
        self.w = 5
        self.v = 3

class C(B):
    r = 0
    def getC(self):
        self.r = self.w-self.v
        print("subtraction",self.r)


obj1 = B()
obj2 = C()
obj1.getA()
obj2.getB()
obj2.getC()
obj1.getB()



