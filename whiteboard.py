#whiteboard without init

class whiteboard:
    length = 0
    breadth = 0
    brand = ""
    pins = 0
    cost = 0

    def setwhiteboard(self):
        self.length = int(input("enter the length"))
        self.breadth = int(input("enter the breadth"))
        self.brand = input("enter the brand")
        self.pins = int(input("enter the no. of pins"))
        self.cost = int(input("enter the cost"))

    def getwhiteboard(self):
        print("length:",self.length,"breadth:",self.breadth,"brand:",self.brand,"pins:",self.brand,"cost:",self.cost)

        

obj = whiteboard()
obj.setwhiteboard()
obj.getwhiteboard()