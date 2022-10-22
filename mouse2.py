#mouse with init

class mouse:
    type = ""
    quality = ""
    brand = ""
    cost = 0

    def __init__(self,type,quality,brand,cost):
        self.type = type
        self.quality = quality
        self.brand = brand
        self.cost =  cost

    def getmouse(self):
        print("Type:",self.type,"quality:",self.quality,"brand:",self.brand,"cost:",self.cost)

    def __del__(self):
        print("contrsuctor is deleted")


obj = mouse("optical","wireless","lenovo",900)
obj.getmouse()


