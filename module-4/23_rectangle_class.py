#Write a Python class named Rectangle constructed by a length 
#and width and a method which will compute the area of a rectangle 

class Rectangle:
    def area(self,length,width):
        print("Area of rectangle:",length*width)

re=Rectangle()
re.area(5,5)
