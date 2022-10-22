class Student:
    stud_roll = 0
    stud_name = ""
    stud_address = ""
    stud_age = 0
    stud_gender = ""

    def setStudent(self):
        self.stud_roll = 123
        self.stud_name = "Ritika"
        self.stud_address = "Howrah"
        self.stud_age = 20
        self.stud_gender = "F"

    def getStudent(self):
        print("roll no:",self.stud_roll)
        print("Name:",self.stud_name)
        print("Address:",self.stud_address)
        print("age:",self.stud_age)
        print("gender:",self.stud_gender)

stud = Student()
stud.setStudent()
stud.getStudent()