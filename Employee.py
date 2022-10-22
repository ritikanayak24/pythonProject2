#Employee without init

class Employee:
    name = ""
    age = 0
    address = ""
    gender = ""
    regno = 0

    def setEmployee(self):
        self.name = input("Enter the name of the employee")
        self.address = input("Enter the address")
        self.age = int(input("Enter the age"))
        self.gender = input("enter the gender")
        self.regno = int(input("enter the reg no:"))


    def getEmployee(self):
        print("Name is {}".format(self.name))
        print("Address is {}".format(self.address))
        print("Gender is {}".format(self.gender))
        print("Age is {}".format(self.age))
        print("regno is {}".format(self.regno))


b = Employee()
b.setEmployee()
b.getEmployee()