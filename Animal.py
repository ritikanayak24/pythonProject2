class Animal:

    def getNameofanimal(self):
        return 0

class dog(Animal):

    def getNameofanimal(self):
      print("dog is an animal")

class lion(Animal):
    def getNameofanimal(self):
        print("lion is an animal")

class cat(Animal):
    def getNameofanimal(self):
        print("cat is an animal")

class cow(Animal):
    def getNameofanimal(self):
        print("cow is an animal")

b=Animal()
b=dog()
b.getNameofanimal()
b=lion()
b.getNameofanimal()
b=cat()
b.getNameofanimal()
b=cow()
b.getNameofanimal()