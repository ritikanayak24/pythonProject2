class Student1:
    stud_roll = 0
    stud_name = ""
    stud_address = ""
    stud_age = 0
    stud_gender = ""

    def setStudent1(self):
        self.stud_roll=int(input("Enter a student roll:"))
        self.stud_age = int(input("enter age"))
        self.stud_name = input("enter name")
        self.stud_gender = input("enter gender")
        self.stud_address = input("enter address")


    def getStudent1(self):
        print("Student roll no is {}".format(self.stud_roll))
        print("student name is {}".format(self.stud_name))
        print("student address is {}".format(self.stud_address))
        print("student gender is {}".format(self.stud_gender))
        print("student age is {}".format(self.stud_age))


stud1 = Student1()
stud1.setStudent1()
stud1.getStudent1()
