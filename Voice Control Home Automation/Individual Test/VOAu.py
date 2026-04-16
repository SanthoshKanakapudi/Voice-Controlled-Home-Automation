# 192.168.3.57
from tkinter import * #type:ignore
from requests import get
url="https://blr1.blynk.cloud/external/api/update?token=__VkcgYtNzUaEwNH7DJAusyudefDZ9aK&"
def turn(pin,case):
    try:
        url1=url+pin+"="+str(case)
        print(url1)
        a=get(url1)
        print(a.status_code)
    except:
        print("First Connect the system to internet")

def allon():
    try:
        turn("v0",1)
        turn("v1",1)
        turn("v2",1)
    except:
        print("First Connect the system to internet")
def alloff():
    try:
        turn("v0",0)
        turn("v1",0)
        turn("v2",0)
    except:
        print("First connect the system to internet")
def main_win():
    win=Tk()
    L1=Label(text="Light 1",padx=10,pady=10,width=10)
    B11=Button(text="ON",padx=5,pady=5,width=5,command=lambda:turn("v0",1))
    B12=Button(text="OFF",padx=5,pady=5,width=5,command=lambda:turn("v0",0))
    L2=Label(text="Light 2",padx=10,pady=10,width=10)
    B21=Button(text="ON",padx=5,pady=5,width=5,command=lambda:turn("v2",1))
    B22=Button(text="OFF",padx=5,pady=5,width=5,command=lambda:turn("v2",0))
    L3=Label(text="Light 3",padx=10,pady=10,width=10)
    B31=Button(text="ON",padx=5,pady=5,width=5,command=lambda:turn("v3",1))
    B32=Button(text="OFF",padx=5,pady=5,width=5,command=lambda:turn("v3",0))
    L4=Label(text="All 3 lights",padx=10,pady=10,width=10)
    B41=Button(text="ON",padx=5,pady=5,width=5,command=allon)
    B42=Button(text="OFF",padx=5,pady=5,width=5,command=alloff)
    L1.grid(row=0,column=0,columnspan=2)
    B11.grid(row=1,column=0)
    B12.grid(row=1,column=1)
    L2.grid(row=2,column=0,columnspan=2)
    B21.grid(row=3,column=0)
    B22.grid(row=3,column=1)
    L3.grid(row=4,column=0,columnspan=2)
    B31.grid(row=5,column=0)
    B32.grid(row=5,column=1)
    L4.grid(row=2,column=2,columnspan=2)
    B41.grid(row=3,column=2)
    B42.grid(row=3,column=3)
    win.mainloop()
main_win()