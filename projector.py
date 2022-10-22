#projector with init

class projector:
    type = ""
    quality = ""
    brand = ""

    def __init__(self, type, quality, brand):
        self.type = type
        self.quality = quality
        self.brand = brand

    def getprojector(self):
        print("Type:", self.type, "quality:", self.quality, "brand:", self.brand)

    def __del__(self):
        print("contrsuctor is deleted")


obj = projector("optical", "wireless", "lenovo")
obj.getprojector()
