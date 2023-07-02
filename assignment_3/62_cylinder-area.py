# Write a Python program to calculate surface volume and 
# area of a cylinder. 

pi =22/7
height = float(input("Enter Height Of Cylinder:-"))
radian = float(input("Enter Radius Of Cylinder:-"))
volume = pi * radian * radian * height
sur_area= ((2*pi*radian)*height) + ((pi*radian**2)*2)

print("Volume Is:-",volume)
print("Surface Area is:-",sur_area)