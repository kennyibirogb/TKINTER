import tkinter as tk
from tkinter import messagebox
import time
import threading #enables running the alarm checking function without freezing the GUI
import pygame #pygame is a library that is used for multimedia applications.
import os

pygame.mixer.init()

def check_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")#retrives the current time in HH:MM format
        if current_time == alarm_time:
            sound_file = "c:\\Users\\Ibirogbakehinde\\Desktop\\TKINTER\\Tic-Tac-Mechanical-Alarm-Clock-2-chosic.com_ (1).mp3"

            if os.path.exists(sound_file):
                pygame.mixer.music.load(sound_file) #Loads the sound file into the pygame music player.
                pygame.mixer.music.play(-1)
                while pygame.mixer.music.get_busy():
                    if set_alarm:
                        pygame.mixer.music.stop()
                        break
                    time.sleep(0.1)  # Prevent CPU overutilization
            else:
                messagebox.showerror("Error", f"Sound file not found: {sound_file}")

            messagebox.showinfo("Alarm", "Time to wake up!")
            break
        time.sleep(1)

def set_alarm():
    alarm_time = f"{hour_entry.get()}:{minute_entry.get()}"
    threading.Thread(target=check_alarm, args=(alarm_time,)).start()
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry('700x800')
root.configure(bg='black')

# Create input fields for hour and minute
hour_label = tk.Label(root, text="Hour (HH):",width=20)
hour_label.pack(padx=20, pady=20)
hour_entry = tk.Entry(root, width=30)
hour_entry.pack(padx=20, pady=20)

minute_label = tk.Label(root, text="Minute (MM):",width=20)
minute_label.pack(padx=20, pady=20)
minute_entry = tk.Entry(root, width=30)
minute_entry.pack(padx=20, pady=20)

# Create a button to set the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

# Start the GUI event loop
root.mainloop()
