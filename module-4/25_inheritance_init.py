#Explain Inheritance in Python with an example?
# What is init? Or What Is A Constructor In Python? 

class Fadher:
    car=0
    bal=0

    def getdata(self):
     self.car=input("Enter car detais:")
     self.bal=input("Enter bank: ")

class Son(Fadher):
    def printdata(self):
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

n=Son()
n.getdata()
n.printdata()

# init is the blocks which we can put the codes
#  in the separate area before the class property.

# Constructors are generally used for instantiating an object.
# The task of constructors is to initialize (assign values) 
# to the data members of the class when an object of class is created.
# In Python the __init__ () method is called the constructor 
# and is always called when an object is created.


        