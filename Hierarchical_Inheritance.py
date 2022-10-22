#Hierarchical Inheritance

class A:
    name = ""
    roll = 0
    address = " "

    def getA(self):
        self.name = "Ritika"
        self.roll = 123
        self.address = "Howrah"


class B(A):
    def getB(self):
        print("Name:", self.name)


class C(A):
    def getC(self):
        print("Roll:", self.roll)


class D(A):
    def getD(self):
        print("address:", self.address)


obj = D()
obj2 = C()
obj3 = B()
obj.getA()
obj2.getA()
obj3.getA()
obj3.getB()
obj2.getC()
obj.getD()







