#keyboard without init

class keyboard:
    type = ""
    quality = ""
    brand = ""

    def setkeyboard(self):
        self.type = input("Enter the type")
        self.quality = input("Enter the quality")
        self.brand = input("enter the brand of the keyboard")

    def getkeyboard(self):
        print("Type is {}".format(self.type))
        print("quality is {}".format(self.quality))
        print("brand is {}".format(self.brand))
        
c = keyboard()
c.setkeyboard()
c.getkeyboard()