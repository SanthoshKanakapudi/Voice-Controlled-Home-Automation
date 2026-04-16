from tkinter import *#type:ignore
import sys
from tkinter.scrolledtext import ScrolledText
from speech_recognition import Microphone as Mp,Recognizer as Rg, UnknownValueError as UVE
import pyttsx3
import threading
import keyboard as kb
from requests import get
""" Successfull """

url="https://blr1.blynk.cloud/external/api/update?token=__VkcgYtNzUaEwNH7DJAusyudefDZ9aK&"
engine = pyttsx3.init()
def clear():
    try:
        tex_to_print.delete(1.0,"end")
    except:
        pass

def turn(pin,case):
    url1=url+pin+"="+str(case)
    print(url1)
    a=get(url1)
    print(a.status_code)
def stoploop():
        #notworking
        if(kb.is_pressed("esc")):
            print(1)
            engine.stop()
def mp3(text):
    imgb.configure(image=img1)
    caption.configure(text="Click to \nspeak again")
    # print(text)
    v=engine.getProperty('voices')
    engine.setProperty('voice',v[1].id)
    thread1 = threading.Thread(target=engine.say, args=(text,))
    thread2= threading.Thread(target=engine.runAndWait)
    thread3= threading.Thread(target=stoploop)
    thread3.start()
    thread1.start()
    thread2.start()
def audio():
    mic=Mp()
    r=Rg()
    try:  
        with mic as source:
            text=r.adjust_for_ambient_noise(source)
            text=r.listen(source)
            tex=r.recognize_google(text)
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
        return mp3("Unable to recognise Try to speak something")
def check(tex):
    if("turn on first light" in tex or "kitchen light on" in tex or "first light on" in tex):
        turn("v0",0)
        return mp3("Ok sure, Kitchen light is on")
    if("turn off first light" in tex or "kitchen light of" in tex or "first light off" in tex):
        turn("v0",1)
        return mp3("Ok sure, Kitchen light is turned of")
    if("exit from app" in tex or "exit" in tex):
        return mp3("Do you want to exit app?")
    if("turn on all" in tex):
        turn("v0",0)
        turn("v1",0)
        turn("v2",0)
        return mp3("Turning on all appliances")
    if("turn off all" in tex):
        turn("v0",1)
        turn("v1",1)
        turn("v2",1)
        return mp3("Turning off all appliances")
    if("turn on red light" in tex or "red light on" in tex):
        turn("v1",0)
        return mp3("Ok got it, Turning on red light")
    if("turn off red light" in tex or "red light off" in tex):
        turn("v1",1)
        return mp3("Ok got it, Turning off red light")
    if("turn on green light" in tex or "green light on" in tex):
        turn("v2",0)
        return mp3("Ok got it, Turning on Green light")
    if("turn off green light" in tex or "green light off" in tex):
        turn("v2",1)
        return mp3("Ok got it, Turning off Green light")
    else:
        return mp3("You said "+tex+" it is not a command")
def audiothread(tex):
    caption.configure(text="Speak now")
    imgb.configure(image=img2)
    tex.insert(END,"\nCommand: ")
    t1=threading.Thread(target=audio)
    t1.start()
main=Tk()
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
hf.mainloop()
main.mainloop()
sys.exit()