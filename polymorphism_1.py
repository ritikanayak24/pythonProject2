class RBI:
    def getRateofInterest(self):
        return 0.0

class SBI(RBI):
    def getRateofInterest(self):
        return 7.1

class HDFC(RBI):
    def getRateofInterest(self):
        return 8.1

class Axis(RBI):
    def getRateofInterest(self):
        return 8.5

s = SBI()
print(s.getRateofInterest())

h=HDFC()
print(h.getRateofInterest())

a=Axis()
print(a.getRateofInterest())

