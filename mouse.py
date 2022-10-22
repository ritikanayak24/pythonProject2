#Mouse with init

class mouse:
    type = ""
    quality = ""
    brand = ""

    def setmouse(self):
        self.type = input("Enter the type")
        self.quality = input("Enter the quality")
        self.brand = input("enter the brand of the mouse")

    def getmouse(self):
        print("Type is {}".format(self.type))
        print("quality is {}".format(self.quality))
        print("brand is {}".format(self.brand))

obj = mouse()
obj.setmouse()
obj.getmouse()
