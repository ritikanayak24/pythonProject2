class Student2:
    stud_roll = 0
    stud_name = ""
    stud_address = ""
    stud_age = 0
    stud_gender = ""

    def setStudent2(self,stud_roll,stud_name,stud_gender,stud_address,stud_age):
        self.stud_roll= stud_roll
        self.stud_age = stud_age
        self.stud_name = stud_name
        self.stud_gender = stud_gender
        self.stud_address = stud_address


    def getStudent2(self):
        print("Student roll no is {}".format(self.stud_roll))
        print("student name is {}".format(self.stud_name))
        print("student address is {}".format(self.stud_address))
        print("student gender is {}".format(self.stud_gender))
        print("student age is {}".format(self.stud_age))


stud2 = Student2()
stud2.setStudent2(12,'Rit','F','hrh',21)
stud2.getStudent2()
