#keyboard with init

class key1:
    type = ""
    quality = ""
    brand = ""

    def __init__(self,type,quality,brand):
        self.type = type
        self.quality = quality
        self.brand = brand

    def getkey1(self):
        print("Type:",self.type,"quality:",self.quality,"brand:",self.brand)

    def __del__(self):
        print("contrsuctor is deleted")


obj = key1("optical","wireless","lenovo")
obj.getkey1()
