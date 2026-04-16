import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import requests
import pyttsx3
import speech_recognition as sr
import serial
import time
import threading


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Automation Interface")
        self.root.geometry("800x600")
        self.color_palette = ["red", "#c3c3c3", "cyan", "white", "black", "green"]
        self.blynk_url = "https://your_blynk_url_here"  # Replace with actual Blynk URL
        self.serial_connected = False
        self.bluetooth_port = "/dev/tty.your_bluetooth_device"  # Update with correct serial port
        self.audio_engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        
        self.setup_ui()
        self.setup_time_update()
        
    def setup_ui(self):
        # Side panel buttons
        self.main_frame = tk.Frame(self.root, bg=self.color_palette[1])
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.side_frame = tk.Frame(self.root, bg=self.color_palette[1], width=100, height=600)
        self.side_frame.grid(row=0, column=0, sticky="ns")
        self.setup_side_panel()

    def setup_side_panel(self):
        buttons = {
            "Home": self.show_home_page,
            "Setup": self.show_setup_page,
            "Buttons": self.show_button_page,
            "Voice": self.show_voice_page,
            "Bluetooth": self.show_bluetooth_page,
        }
        y_position = 100

        for name, command in buttons.items():
            button = tk.Button(self.side_frame, text=name, fg=self.color_palette[0], bd=0,
                               font=('bold', 15), bg=self.color_palette[1], command=command)
            button.place(x=10, y=y_position)
            y_position += 50

        self.time_label = tk.Label(self.side_frame, text="", font=("bold", 12), bg=self.color_palette[1])
        self.time_label.place(x=10, y=10)

    def setup_time_update(self):
        self.update_time()
        self.root.after(1000, self.update_time)

    def update_time(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.time_label.configure(text=current_time)

    def show_home_page(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Home Page", font=("bold", 20)).pack(pady=10)

    def show_setup_page(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Setup Page", font=("bold", 20)).pack(pady=10)

    def show_button_page(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Button Interface", font=("bold", 20)).pack(pady=10)
        
        # Example button to control an IoT device via Blynk
        self.button_control = tk.Button(self.main_frame, text="Toggle LED", command=self.toggle_led)
        self.button_control.pack(pady=10)

    def toggle_led(self):
        # Sample function to toggle LED via Blynk
        try:
            response = requests.get(f"{self.blynk_url}/update/V0?value=1")  # Toggle LED on
            if response.status_code == 200:
                messagebox.showinfo("Success", "LED toggled!")
            else:
                messagebox.showerror("Error", "Failed to toggle LED.")
        except requests.RequestException as e:
            messagebox.showerror("Network Error", f"Failed to connect to Blynk server.\n{e}")

    def show_voice_page(self):
        self.clear_main_frame()
        VoicePage(self.main_frame, self.audio_engine, self.recognizer)

    def show_bluetooth_page(self):
        self.clear_main_frame()
        BluetoothPage(self.main_frame, self.bluetooth_port)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


class VoicePage:
    def __init__(self, parent_frame, audio_engine, recognizer):
        self.parent_frame = parent_frame
        self.audio_engine = audio_engine
        self.recognizer = recognizer
        self.setup_voice_interface()

    def setup_voice_interface(self):
        tk.Label(self.parent_frame, text="Voice Command Interface", font=("bold", 20)).pack(pady=10)
        self.text_area = ScrolledText(self.parent_frame, width=40, height=10)
        self.text_area.pack(pady=10)

        self.speak_button = tk.Button(self.parent_frame, text="Speak", command=self.process_voice_command)
        self.speak_button.pack(pady=5)

    def process_voice_command(self):
        mic = sr.Microphone()
        try:
            with mic as source:
                audio_data = self.recognizer.listen(source)
                command_text = self.recognizer.recognize_google(audio_data).lower()
                self.text_area.insert("end", f"Command: {command_text}\n")
                self.execute_command(command_text)
        except sr.UnknownValueError:
            self.text_area.insert("end", "Could not understand the audio.\n")

    def execute_command(self, command_text):
        if "hello" in command_text:
            self.speak("Hello! How can I assist?")
        elif "turn on light" in command_text:
            # Insert code to turn on the light, e.g., calling an API
            self.speak("Turning on the light.")
        else:
            self.speak(f"You said: {command_text}")

    def speak(self, text):
        self.audio_engine.say(text)
        threading.Thread(target=self.audio_engine.runAndWait).start()


class BluetoothPage:
    def __init__(self, parent_frame, port):
        self.parent_frame = parent_frame
        self.port = port
        self.serial_connection = None
        self.setup_bluetooth_interface()

    def setup_bluetooth_interface(self):
        tk.Label(self.parent_frame, text="Bluetooth Interface", font=("bold", 20)).pack(pady=10)
        
        self.connect_button = tk.Button(self.parent_frame, text="Connect", command=self.connect_bluetooth)
        self.connect_button.pack(pady=5)
        
        self.disconnect_button = tk.Button(self.parent_frame, text="Disconnect", command=self.disconnect_bluetooth)
        self.disconnect_button.pack(pady=5)

    def connect_bluetooth(self):
        try:
            self.serial_connection = serial.Serial(self.port, baudrate=9600, timeout=1)
            messagebox.showinfo("Bluetooth", "Connected to Bluetooth device.")
        except serial.SerialException:
            messagebox.showerror("Bluetooth", "Failed to connect to Bluetooth device.")

    def disconnect_bluetooth(self):
        if self.serial_connection:
            self.serial_connection.close()
            messagebox.showinfo("Bluetooth", "Bluetooth disconnected.")
        else:
            messagebox.showerror("Bluetooth", "No active Bluetooth connection.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
