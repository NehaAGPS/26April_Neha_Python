data={}
data2={}
fl=open('student.txt','a+')
def std():
    keys=("ID","Name","Branch","City")
    key1=input("Enter Your Main Key:-")   
    for j in range(len(keys)):
        val=input(f"Enter your value for {keys[j]}:-")
        data2[keys[j]]=val
        data[key1]=data2.copy()
    fl.write(str(data))
        
    

def search():
    stdata=dict()
    fl=open("student.txt",'r+')
    stdata=fl.read()
    #print(stdata)
    dt=eval(stdata)
    v=input("Search main Key:-")
    if v in dt:
        print(dt[v])

def collagestaff():
    n=int(input("Enter Number Of Student:-"))
    keys=("ID","Name","Branch","City")
    for i in range(n):
        key1=input("Enter Your Main Key:-")   
        for j in range(len(keys)):
            val=input(f"Enter your value for {keys[j]}:-")
            data2[keys[j]]=val
            data[key1]=data2.copy()
    fl.write(str(data))

y="y"
while y!="n":         
    print("Student Registration System")
    print("1.Student")
    print("2.Collage Staff")
    choose=int(input("Enter Your Role:-"))
    if choose == 1:
        y="y"
        while y!="n":
            print("1.Enter Data")
            print("2.Search Data")
            d=int(input("Enter Your choise:-"))
            if d == 1:
                print("Welcome Student Enter Your Data")
                std()
            else:
                search()
            y=input("Do You Wan't Countinue:-")
        
    elif choose == 2:
        y="y"
        while y!="n":
            print("Welcome Collage Staff Desk")
            print("1.Enter Student Data")
            print("2.Search Student Data")
            m=int(input("Collage Enter Your Choise:- "))
            if m == 1:
                print("Collage Staff Enter Student Data")
                collagestaff()
            else:
                search()
            y=input("Do You Wan't to countinue:-")
    y=input("Do You Wan't to countinue:-")         
            









