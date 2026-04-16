from tkinter import *#type:ignore
import threading
from pyttsx3 import init
from speech_recognition import Microphone as Mp,Recognizer as Rg, UnknownValueError as UVE
import serial
audio_engine = init()
def connectblue():
    global ser 
    try:
        device_address = '98:D3:31:F6:80:EB'
        ser = serial.Serial('COM7', baudrate=9600)
        try:
           print("Connected")
        except:pass
    except:
        try:
           print("Not connected!")
        except:pass
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
            print("Bluetooth Not connected!")
        except:pass
def mp3(text):
        v=audio_engine.getProperty('voices')
        thread1 = threading.Thread(target=audio_engine.say, args=(text,))
        thread2= threading.Thread(target=audio_engine.runAndWait)
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
                print(tex)
            if(tex=="yes"):
                exit()
            tex_to_print.insert(END,tex)#type:ignore
        except(UVE):
            return mp3("Speak again!")
        except(ValueError):
            return mp3("Nothing")
        except:
            return mp3("Unable to recognise Try to speak again")