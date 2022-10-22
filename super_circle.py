class C:
    r=0
    def __init__(self):
        self.r = int(input("Enter the radius"))

class Area(C):
    a=0
    def __init__(self):
        super().__init__()
        self.a = 2*3.14*self.r

    def display(self):
        print("area of circle:",self.a)

b = Area()
b.display()



