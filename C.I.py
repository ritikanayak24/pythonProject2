import math
p=int(input("enter the value of principal"))
r=float(input("enter rate of interest"))
t=int(input("enter time"))
n=int(input("enter year"))
      c=(1+(r/n))
      a=t*n
      d=math.pow(c,a)
print("C.I:",d)