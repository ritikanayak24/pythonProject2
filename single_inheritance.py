#singleinheritance

class Student3:  #parent,base,super
    stud_roll = 0
    stud_name = ""
    stud_address = ""
    stud_age = 0
    stud_gender = ""

    def getStudent3(self):
        self.stud_roll = 123
        self.stud_name = "Ritika"
        self.stud_address = "Howrah"
        self.stud_age = 20
        self.stud_gender = "F"


class Display(Student3):
    def getDisplay(self):
        print("roll no:", self.stud_roll)
        print("Name:", self.stud_name)
        print("Address:", self.stud_address)
        print("age:", self.stud_age)
        print("gender:", self.stud_gender)


obj = Display()
obj.getStudent3()
obj.getDisplay()

