#whiteboard with init

class white:
    length = 0
    breadth = 0
    brand = ""
    pins = 0
    cost = 0

    def __init__(self,length,breadth,brand,pins,cost):
        self.length = length
        self.breadth = breadth
        self.brand = brand
        self.pins = pins
        self.cost = cost

    def getwhite(self):
        print("length",self.length,"breadth",self.breadth,"brand",self.brand,"pins",self.pins,"cost",self.cost)

    def __del__(self):
        print("the contructor is deleted")

obj = white(21,34,"lenovo",4,200)
obj.getwhite()

