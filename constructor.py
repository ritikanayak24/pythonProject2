class Constructor:
    def __init__(self):
        print("this is a constructor")

    def __del__(self):
        print("this ia a destructor")

def Create_Constructor():
   print("creating object")
   c = Constructor()
   return c

obj = Create_Cons
print(obj)