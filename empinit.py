#Employee with init

class empinit:
    name = ""
    age = 0
    regno = 0
    address = ""
    gender = ""

    def __init__(self,age,name,regno,address,gender):
        self.name = name
        self.age = age
        self.regno = regno
        self.address = address
        self.gender = gender

    def getempinit(self):
        print("Name is ",self.name)
        print("Age is",self.age)
        print("regno is",self.regno)
        print("address is",self.address)
        print("gender is",self.gender)

    def __del__(self):
        print("the employee file is deleted")

obj = empinit(20,"Ritika",190,"Howrah","F")
obj.getempinit()
