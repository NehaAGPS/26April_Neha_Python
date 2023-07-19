#How to Define a Class in Python? What Is Self? 
# Give An Example Of A Python Class..!


#A class in Python can be defined using the class keyword.
#As per the syntax above, a class is defined using the class keyword 
# followed by the class name and : operator after the class name, 
#which allows you to continue in the next indented line to 
# define class members. 

# In object-oriented programming, whenever we define methods for a class, 
# we use self as the first parameter in each case.

class student:
    id=101
    nm='neha'

    def getdata(self):
        print("This is Student Class.")

# Objcet 
st=student()
print(st.id)
print(st.nm)
st.getdata()

