from tkinter import *#type:ignore
import sys
from requests import get
from tkinter.scrolledtext import ScrolledText
import threading
from pyttsx3 import init
from speech_recognition import Microphone as Mp,Recognizer as Rg, UnknownValueError as UVE
import keyboard as kb
import serial
import time
audio_engine = init()
# url="https://blr1.blynk.cloud/external/api/update?token=__VkcgYtNzUaEwNH7DJAusyudefDZ9aK&"
url="https://blr1.blynk.cloud/external/api/update?token=gulFNE2AOhXAgFWszOxE4kRF7ghDuaq7&"
coli=["red","#c3c3c3","cyan","white","black","green"]#Colourlist
def connectblue():
    global ser 
    try:
        device_address = '98:D3:31:F6:80:EB'
        ser = serial.Serial('COM7', baudrate=9600)
        try:
            blue_eror.configure(text="device connected to "+device_address)
        except:pass
    except:
        try:
            blue_eror.configure(text="First connect to a device!!")
        except:pass
def hideind():
    h_ind.config(bg=coli[1])
    b_ind.config(bg=coli[1])
    v_ind.config(bg=coli[1])
    s_ind.config(bg=coli[1])
    bl_ind.config(bg=coli[1])
    
def indicate(x,y):
    #Here x is a indicator label
    #y is a page to show
    hideind()
    x.config(bg=coli[2])
    delpage()
    y()#y is a page
def turn(pin,case):
    try:
        url1=url+pin+"="+str(case)
        if(case==1):
            pass
        elif(case==0):
            pass
        # print(url1)
        get(url1)
        # print(a.status_code)
        try:
            checkin.configure(text="Connected to Internet")
        except:
            pass
    except:
        checkin.configure(text="First Connect the system to internet")
        print("First Connect the system to internet")

def sendblue(z):
    try:
        if(z==1):
            ser.write(b'2')
        if(z==2):
            ser.write(b'1')
        if(z==3):
            ser.write(b'4')
        if(z==4):
            ser.write(b'3')
        if(z==5):
            ser.write(b'6')
        if(z==6):
            ser.write(b'5')
    except:
        try:
            blue_eror.configure(text="First connect to a device!!")
        except:pass

def allon():
    try:
        turn("v0",0)
        turn("v1",0)
        turn("v2",0)
        turn("v3",0)
    except:
        print("First Connect the system to internet")
def alloff():
    try:
        turn("v0",1)
        turn("v1",1)
        turn("v2",1)
        turn("v3",1)
    except:
        print("First connect the system to internet")
def allon_via_blue(x):
    if(x==1):
        sendblue(1)
        sendblue(3)
        sendblue(5)
    if(x==2):
        sendblue(2)
        sendblue(4)
        sendblue(6)
#Defining Pages
def homepage():
    hf=Frame(main)
    hf.config(bg=coli[1])
    a="""Commands for Light 1
    To ON:
    1) First Light on
    2)Turn on First light
    3)First Socket on
    Kitchen light on
    To OFF:
    1)Turn off first light
    2)Kitchen light off
    3)First socket off
    4)Kitchen light off"""
    b="""Commands for Light 2
    To ON:
    1) Second Light on
    2)Turn on Second light
    3)Second Socket on
    Kitchen light on
    To OFF:
    1)Turn off second light
    2)second light off
    3)second socket off
    """
    c="""Commands for Light 3
    To ON:
    1) third Light on
    2)Turn on third light
    3)third Socket on
    Kitchen light on
    To OFF:
    1)Turn off third light
    2)third light off
    3)third socket off
    """
    com1=Label(hf,text=a,)
    com2=Label(hf,text=b,)
    com3=Label(hf,text=c,)
    com1.grid(row=0,column=0)
    com2.grid(row=0,column=1)
    com3.grid(row=0,column=2)
    hf.grid()
def buttonpage():
    def button_highlight(x,y):
        x.configure(bg=coli[0])
        y.configure(bg=coli[3])
    def alloffhigh():
        B12.configure(bg=coli[0])
        B22.configure(bg=coli[0])
        B32.configure(bg=coli[0])
        B11.configure(bg=coli[3])
        B21.configure(bg=coli[3])
        B31.configure(bg=coli[3])
        button_highlight(B42,B41)
    def allonhigh():
        B12.configure(bg=coli[3])
        B22.configure(bg=coli[3])
        B32.configure(bg=coli[3])
        B11.configure(bg=coli[0])
        B21.configure(bg=coli[0])
        B31.configure(bg=coli[0])
        button_highlight(B41,B42)
    global checkin
    hf=Frame(main) 
    main.config(bg=coli[1])
    hf.config(bg=coli[1])
    T1=Label(hf,text="Buttons Interface",padx=10,pady=10,width=45,border=1,bg='blue',fg=coli[0],font=("bold",20),highlightthickness=2,highlightbackground=coli[4])
    L1=Label(hf,text="Light 1",padx=10,pady=10,width=10,font=("bold"))
    B11=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[turn("v0",0),button_highlight(B11,B12)],font=("bold"),highlightthickness=2,highlightbackground=coli[4])
    B12=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[turn("v0",1),button_highlight(B12,B11)],font=("bold"))
    L2=Label(hf,text="Light 2",padx=10,pady=10,width=10,font=("bold"))
    B21=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[turn("v1",0),button_highlight(B21,B22)],font=("bold"))
    B22=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[turn("v1",1),button_highlight(B22,B21)],font=("bold"))
    L3=Label(hf,text="Light 3",padx=10,pady=10,width=10,font=("bold"))
    B31=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[turn("v2",0),button_highlight(B31,B32)],font=("bold"),)
    B32=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[turn("v2",1),button_highlight(B32,B31)],font=("bold"))
    L4=Label(hf,text="All 3 lights",padx=10,pady=10,width=10,font=("bold"))
    B41=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[allon(),allonhigh()],font=("bold"))
    B42=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[alloff(),alloffhigh()],font=("bold"))
    checkin=Label(hf,text="")
    #Buttonpage 1 Placement
    T1.grid(row=0,column=0,columnspan=2)
    L1.grid(row=1,column=0,columnspan=2)
    B11.grid(row=2,column=0)
    B12.grid(row=2,column=1)
    L2.grid(row=3,column=0,columnspan=2)
    B21.grid(row=4,column=0)
    B22.grid(row=4,column=1)
    L3.grid(row=5,column=0,columnspan=2)
    B31.grid(row=6,column=0)
    B32.grid(row=6,column=1)
    L4.grid(row=7,column=0,columnspan=2)
    B41.grid(row=8,column=0)
    B42.grid(row=8,column=1)
    checkin.grid()
    hf.grid()
def Bluetoothpage():
    def button_highlight(x,y):
        x.configure(bg=coli[5])
        y.configure(bg=coli[3])
    def alloffhigh():
        B12.configure(bg=coli[5])
        B22.configure(bg=coli[5])
        B32.configure(bg=coli[5])
        B11.configure(bg=coli[3])
        B21.configure(bg=coli[3])
        B31.configure(bg=coli[3])
        button_highlight(B42,B41)
    def allonhigh():
        B12.configure(bg=coli[3])
        B22.configure(bg=coli[3])
        B32.configure(bg=coli[3])
        B11.configure(bg=coli[5])
        B21.configure(bg=coli[5])
        B31.configure(bg=coli[5])
        button_highlight(B41,B42)
    hf=Frame(main) 
    main.config(bg=coli[1])
    hf.config(bg=coli[1])
    T1=Label(hf,text="BT Buttons Interface",padx=10,pady=10,width=45,border=1,bg='blue',fg=coli[0],font=("bold",20),highlightthickness=2,highlightbackground=coli[4])
    L1=Label(hf,text="Light 1",padx=10,pady=10,width=10,font=("bold"))
    B11=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[sendblue(1),button_highlight(B11,B12)],font=("bold"),highlightthickness=2,highlightbackground=coli[4])
    B12=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[sendblue(2),button_highlight(B12,B11)],font=("bold"))
    L2=Label(hf,text="Light 2",padx=10,pady=10,width=10,font=("bold"))
    B21=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[sendblue(3),button_highlight(B21,B22)],font=("bold"))
    B22=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[sendblue(4),button_highlight(B22,B21)],font=("bold"))
    L3=Label(hf,text="Light 3",padx=10,pady=10,width=10,font=("bold"))
    B31=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[sendblue(5),button_highlight(B31,B32)],font=("bold"),)
    B32=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[sendblue(6),button_highlight(B32,B31)],font=("bold"))
    L4=Label(hf,text="All 3 lights",padx=10,pady=10,width=10,font=("bold"))
    B41=Button(hf,text="ON",padx=5,pady=5,width=30,command=lambda:[allon_via_blue(1),allonhigh()],font=("bold"))
    B42=Button(hf,text="OFF",padx=5,pady=5,width=30,command=lambda:[allon_via_blue(2),alloffhigh()],font=("bold"))
    #Buttonpage 1 Placement
    global blue_eror
    blue_eror=Label(hf,text="",padx=10,pady=10,width=45,border=1,bg='white',fg="red")
    blue_eror.grid(row=0,column=0,columnspan=2)
    T1.grid(row=1,column=0,columnspan=2)
    L1.grid(row=2,column=0,columnspan=2)
    B11.grid(row=3,column=0)
    B12.grid(row=3,column=1)
    L2.grid(row=4,column=0,columnspan=2)
    B21.grid(row=5,column=0)
    B22.grid(row=5,column=1)
    L3.grid(row=6,column=0,columnspan=2)
    B31.grid(row=7,column=0)
    B32.grid(row=7,column=1)
    L4.grid(row=8,column=0,columnspan=2)
    B41.grid(row=9,column=0)
    B42.grid(row=9,column=1)
    connectblue()
    hf.grid()
def voicepage(): 
    global tex_to_print
    def clear():
        try:
            tex_to_print.delete(1.0,"end")
        except:
            pass

    def stoploop():
            #notworking
            if(kb.is_pressed("esc")):
                print(1)
                audio_engine.stop()
    def mp3(text):
        imgb.configure(image=img1)
        caption.configure(text="Click to \nspeak again")
        # print(text)
        v=audio_engine.getProperty('voices')
        # audio_engine.setProperty('voice',v[1].id)
        thread1 = threading.Thread(target=audio_engine.say, args=(text,))
        thread2= threading.Thread(target=audio_engine.runAndWait)
        thread3= threading.Thread(target=stoploop)
        thread3.start()
        thread1.start()
        thread2.start()
    def audio():
        mic=Mp()
        r=Rg()
        try:  
            with mic as source:
                text=r.listen(source)
                tex=r.recognize_google(text)
                tex=str(tex)
                tex.lower()
            # print(tex)
            if(tex=="yes"):
                exit()
            tex_to_print.insert(END,tex)#type:ignore
            check(tex)
        except(UVE):
            return mp3("Speak again!")
        except(ValueError):
            return mp3("Nothing")
        except:
            return mp3("Unable to recognise Try to speak again")
    def check(tex):
        tex=tex.lower()
        f_l=["turn on first","first socket on","activate first light","turn on first flight","first light on"]
        fo_l=["turn off first","first socket of","deactivate the first","turn of first flight","first light of"]
        
        if("How are" in tex or "are you" in tex):
            return mp3("Hello there! I'm Fine How can I assist?")
        for item in f_l:
            if(item in tex):
                turn("v0",0)
                try:
                    sendblue(1)
                except:pass
                return mp3("Ok sure, First light is on")
        for item in fo_l:
            if(item in tex):
                turn("v0",1)
                try:
                    sendblue(2)
                except:pass
                return mp3("Ok sure, First light is turned off")
        if("turn on second light" in tex or "red light on" in tex or "second light on" in tex or "second socket on" in tex):
            turn("v1",0)
            try:
                sendblue(3)
            except:pass
            return mp3("Ok got it, Turning on Second light")
        if("turn off second light" in tex or "second light off" in tex or "second socket of" in tex):
            turn("v1",1)
            try:
                sendblue(4)
            except:pass
            return mp3("Ok got it, Turning off second light")
        if("turn on green light" in tex or "green light on" in tex):
            turn("v2",0)
            try:
                sendblue(5)
            except:pass
            return mp3("Ok got it, Turning on Green light")
        if("turn off green light" in tex or "green light off" in tex):
            turn("v2",1)
            try:
                sendblue(6)
            except:pass
            return mp3("Ok got it, Turning off Green light")
        if("turn on all" in tex):
            turn("v0",0)
            turn("v1",0)
            turn("v2",0)
            try:
                sendblue(1)
                sendblue(3)
                sendblue(5)
            except:pass
            return mp3("Turning on all appliances") 
        if("turn off all" in tex):
            turn("v0",1)
            turn("v1",1)
            turn("v2",1)
            try:
                sendblue(2)
                sendblue(4)
                sendblue(6)
            except:pass
            return mp3("Turning off all appliances")
        if("exit from app" in tex or "exit" in tex):
            return mp3("Do you want to exit app?")
        else:
            return mp3("You said "+tex+" it is not a command")
    def audiothread(tex):
        caption.configure(text="Speak now")
        imgb.configure(image=img2)
        tex.insert(END,"\nCommand: ")
        t1=threading.Thread(target=audio)
        t1.start()
    hf=Frame(main)
    hf.config(bg="cyan")
    frame1=Frame(hf,width=100,height=600,highlightbackground="black",highlightthickness=2)
    frame2=Frame(hf,width=500,height=600,highlightbackground="black",highlightthickness=2)
    img1 =PhotoImage(file="C:\\Users\\kanak\\Desktop\\Timepass\\Python\\VoiceAutomation\\spicon.png")
    img2 =PhotoImage(file="C:\\Users\\kanak\\Desktop\\Timepass\\Python\\VoiceAutomation\\images.png")
    imgb=Button(frame1,image=img1,command=lambda:audiothread(tex_to_print))
    tex_to_print=ScrolledText(frame2,pady=100,padx=10)
    imgb.grid(row=8,column=0,rowspan=3)
    caption=Label(frame1,text="click\n to speak")
    cl=Button(frame1,text="clear",command=clear)
    caption.grid()
    tex_to_print.grid()
    cl.grid()
    frame1.grid(row=0,column=0)
    frame2.grid(row=0,column=1)
    hf.grid()
    # connectblue()
    hf.mainloop()
def setuppage():
    hf=Frame(main)
    inlab=Label(hf,text="Enter your URL: ")
    e1=Entry(hf,width=40)
    inlab.grid()
    e1.grid()
    hf.grid()
#deleting page
def delpage():
    for page in main.winfo_children():
        page.grid_forget()
def changetime():
    timelabel.configure(text=time.ctime()[11:20])
    win.after(1000,changetime)
win=Tk()
win.config()
win.title("Voice Automation")
win.geometry("800x600")
#Options Frame
opframe=Frame(win,bg=coli[1])
timelabel=Label(text="")
opframe.grid(row=0,column=0)
opframe.grid_propagate(False)
opframe.configure(width=100,height=600)
#Widgets
home=Button(opframe,text="Home",fg=coli[0],bd=0,font=('bold',15),bg=coli[1],command=lambda:indicate(h_ind,homepage))
h_ind=Label(opframe,text=" ",bg=coli[1])
h_ind.place(x=3,y=100,width=5,height=40)
home.place(x=10,y=100)

setup=Button(opframe,text="Setup",fg=coli[0],bd=0,font=('bold',15),bg=coli[1],command=lambda:indicate(s_ind,setuppage))
s_ind=Label(opframe,text="",bg=coli[1])
s_ind.place(x=3,y=150,width=5,height=40)
setup.place(x=10,y=150)

buttons=Button(opframe,text="Buttons",fg=coli[0],bd=0,font=('bold',15),bg=coli[1],command=lambda:indicate(b_ind,buttonpage))
b_ind=Label(opframe,text=" ",bg=coli[1])
b_ind.place(x=3,y=200,width=5,height=40)
buttons.place(x=10,y=200)

voice=Button(opframe,text="Voice",fg=coli[0],bd=0,font=('bold',15),bg=coli[1],command=lambda:indicate(v_ind,voicepage))
voice.place(x=10,y=250)
v_ind=Label(opframe,text=" ",bg=coli[1])
v_ind.place(x=3,y=250,width=5,height=40)

blue=Button(opframe,text="Bluetooth\nButtons",fg=coli[0],bd=0,font=('bold',15),bg=coli[1],command=lambda:indicate(bl_ind,Bluetoothpage))
blue.place(x=10,y=300)
bl_ind=Label(opframe,text=" ",bg=coli[1])
bl_ind.place(x=3,y=300,width=5,height=40)

#Main Frame
main=Frame(win,highlightbackground=coli[4],highlightthickness=2)

main.grid(row=0,column=1)
main.grid_propagate(False)
main.configure(width=700,height=600)
win.eval('tk::PlaceWindow . center')
timelabel.place(x=10,y=10)
t1=threading.Thread(target=changetime())
t1.start()
win.mainloop()
sys.exit()