class Employee:
    __empid = 0
    __empname = ""
    __empage = 0
    __empdesig = ""
    __empAddress = ""

    def setempid(self,id):
        self.__empid = id

    def getempid(self):
        return self.__empid

    def setempname(self,name):
        self.__empname = name

    def getempname(self):
        return self.__empname

    def setempage(self,age):
        self.__empage = age

    def getempage(self):
        return self.__empage

    def setempdesig(self,desig):
        self.__empdesig = desig

    def getempdesig(self):
        return self.__empdesig

    def setempaddress(self,address):
        self.__empAddress = address

    def getempaddress(self):
        return self.__empAddress

e=Employee()
e.setempid(432)
print(e.getempid())
e.setempname("Ritika")
print(e.getempname())
e.setempage(20)
print(e.getempage())
e.setempdesig("EMP")
print(e.getempdesig())
e.setempaddress("Howrah")
print(e.getempaddress())