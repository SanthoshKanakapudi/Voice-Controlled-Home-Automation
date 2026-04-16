from pyttsx3 import init
from speech_recognition import Microphone as Mp,Recognizer as Rg,UnknownValueError as UVE
from requests import get
from tkinter import *#type:ignore
url="https://blr1.blynk.cloud/external/api/update?token=__VkcgYtNzUaEwNH7DJAusyudefDZ9aK&"
def mp3(text):
    print(text)
    speak=init()
    # v=speak.getProperty('voices')
    speak.setProperty("rate",150)
    speak.say(text)
    speak.runAndWait()
def audio(c): 
    print(c)
    mic=Mp()
    r=Rg()
    try:  
        with mic as source:
            text=r.listen(source)
            tex=r.recognize_google(text)
        # print(tex)
        if(tex=="yes"):
            exit()
        check(tex)
    except(UVE):
        return mp3("Speak again!")
    except(ValueError):
        return mp3("Nothing")
    except:
        return mp3("Unable to recognise Try to speak something")
    
def turn(pin,case):
    url1=url+pin+"="+str(case)
    print(url1)
    a=get(url1)
    print(a.status_code)
def check(tex):
    if("turn on first light" in tex or "kitchen light on" in tex):
        turn("v0",0)
        return mp3("Ok sure, Kitchen light is on")
    if("turn off first light" in tex or "kitchen light off" in tex):
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
        return mp3("Try to give correct command")
win=Tk()
win.geometry("700x600")
voicepage1=Frame(win)
igm = PhotoImage(file="C:\\Users\\kanak\\Desktop\\Timepass\\Python\\Tkinter\\Voice icon.gif")
imgb=Button(voicepage1, image=igm)
imgb.pack()
voicepage1.grid()
win.mainloop()