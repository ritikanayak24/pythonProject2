#Multiple_inheritance

class A:
    x = 0
    y = 0
    def setA(self):
        self.x = 4
        self.y = 2

class B(A):

     z = 0
     def setB(self):
         self.z = self.x + self.y



class C(A):
    w = 0
    def setC(self):
        self.w = self.x - self.y

class D(B,C):
    f = 0
    def getD(self):
        self.f = self.w * self.z
        print("subtraction:", self.w)
        print("addition:", self.z)
        print("multiply:",self.f)

obj3 = D()
obj3.setA()
obj3.setB()
obj3.setC()
obj3.getD()