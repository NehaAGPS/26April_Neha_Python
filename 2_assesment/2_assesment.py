import tkinter
from tkinter import ttk,messagebox


window=tkinter.Tk()
window.title("Pharmacy Management System")
window.geometry("600x700")
window.config(background='white')

tkinter.Checkbutton(text='ADMIN',font='Fixedsys 15',fg='red').grid(row=1,column=2,sticky='w')
tkinter.Checkbutton(text='PHARMACY MANAGER',font='Fixedsys 15',fg='red').grid(row=2,column=2,sticky='w')

tkinter.Label(text="~~~ ADMIN ~~~",font='Fixedsys 15',fg='red').grid(row=4,column=1,sticky='w')
tkinter.Checkbutton(text='Can Ragister',font='Fixedsys 15',fg='red').grid(row=6,column=2,sticky='w')
tkinter.Checkbutton(text='Can Login',font='Fixedsys 15',fg='red').grid(row=7,column=2,sticky='w')
tkinter.Checkbutton(text='Can View All Manager',font='Fixedsys 15',fg='red').grid(row=8,column=2,sticky='w')
tkinter.Checkbutton(text='Can View All Medicine',font='Fixedsys 15',fg='red').grid(row=9,column=2,sticky='w')

tkinter.Label(text="~~~ MANAGER ~~~",font='Fixedsys 15',fg='red').grid(row=11,column=1,sticky='w')
tkinter.Checkbutton(text='Can Ragister',font='Fixedsys 15',fg='red').grid(row=13,column=2,sticky='w')
tkinter.Checkbutton(text='Can Login',font='Fixedsys 15',fg='red').grid(row=14,column=2,sticky='w')
tkinter.Checkbutton(text='Can Add Medicine',font='Fixedsys 15',fg='red').grid(row=15,column=2,sticky='w')
tkinter.Checkbutton(text='Can View Medicine',font='Fixedsys 15',fg='red').grid(row=16,column=2,sticky='w')
tkinter.Checkbutton(text='Can Delete Medicine',font='Fixedsys 15',fg='red').grid(row=17,column=2,sticky='w')

tkinter.Label(text="").grid(row=18,column=1,sticky='w')
tkinter.Label(text="________Medicine Detail_______",font='Fixedsys 15',fg='green').grid(row=19,column=2,sticky='w')
tkinter.Label(text="Sr.No.:  01",font='Fixedsys 15',fg='blue').grid(row=20,column=1,sticky='w')
tkinter.Label(text="Medicine Name:  Den P",font='Fixedsys 15',fg='blue').grid(row=21,column=1,sticky='w')
tkinter.Label(text="Qty:  10*10",font='Fixedsys 15',fg='blue').grid(row=22,column=1,sticky='w')
tkinter.Label(text="Added Date: 8/6/2022 ",font='Fixedsys 15',fg='blue').grid(row=23,column=1,sticky='w')
tkinter.Label(text="Added By:  2",font='Fixedsys 15',fg='blue').grid(row=24,column=1,sticky='w')
tkinter.Label(text="Price:  20",font='Fixedsys 15',fg='blue').grid(row=25,column=1,sticky='w')

tkinter.Label(text="").grid(row=26,column=1,sticky='w')
tkinter.Label(text="________Manager Detail_______",font='Fixedsys 15',fg='green').grid(row=27,column=2,sticky='w')
tkinter.Label(text="Sr.No. : ",font='Fixedsys 15',fg='blue').grid(row=28,column=1,sticky='w')
tkinter.Label(text=" 1 ",font='Fixedsys 15',fg='blue').grid(row=29,column=1,sticky='w')
tkinter.Label(text=" 2 ",font='Fixedsys 15',fg='blue').grid(row=30,column=1,sticky='w')
tkinter.Label(text="Manager Name",font='Fixedsys 15',fg='blue').grid(row=28,column=2,sticky='w')
tkinter.Label(text=" Ramesh ",font='Fixedsys 15',fg='blue').grid(row=29,column=2,sticky='w')
tkinter.Label(text=" Jayesh ",font='Fixedsys 15',fg='blue').grid(row=30,column=2,sticky='w')
tkinter.Label(text="Pharmacy Name",font='Fixedsys 15',fg='blue').grid(row=28,column=3,sticky='w')
tkinter.Label(text="Jayraj Pharmacy",font='Fixedsys 15',fg='blue').grid(row=29,column=3,sticky='w')
tkinter.Label(text="Tomato Pharmacy",font='Fixedsys 15',fg='blue').grid(row=30,column=3,sticky='w')

tkinter.mainloop()

