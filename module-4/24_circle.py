#Write a Python class named Circle constructed by a radius 
#and two methods which will compute the area and the 
#perimeter of a circle. 


from math import pi
class Circle:
    r=int(input("Enter radius:"))

    def Area(self):
      print("Area of circle:",pi*self.r**2)

    def perimeter(self):
      print("Perimeter of circle:",2*pi*self.r)

c=Circle()
c.Area()
c.perimeter()