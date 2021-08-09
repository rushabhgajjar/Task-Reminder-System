# TASK REMINDER SYSTEM

"""
Desk job of corporate employees for prolong period of time could lead to body stiffness and other issues
The 3 tasks are eye relaxation, physical movement and drink water
The reminder is given to user by playing different tunes as per task
Data is logged in a file along with timestamp once the task is completed
"""

from pygame import mixer
import datetime
import time
import os


def play_alarm(file_name, notification):
    mixer.init()                                 # start the player
    mixer.music.load(file_name)                  # Loads tune in the player
    mixer.music.set_volume(0.9)                  # Set volume for the tune
    mixer.music.play(-1)                         # Play tune
    print(notification)


def stop_alarm(stopper):
    while True:
        a = input(f"Once completed please type '{stopper}' to stop: ")
        if a.lower() == stopper:
            mixer.music.stop()
            break


def log(message):
    with open("my_log.txt", "a") as f:
        f.write(str(real_time) + f"   {message}\n")  # Logs data in text file for activity performed & time for the same


eyes_time = datetime.datetime.now()
eyes = datetime.timedelta(minutes=3)              # Reminder for eye relaxation is set to 3 minutes
physical_time = datetime.datetime.now()
physical = datetime.timedelta(minutes=5)          # Reminder for physical movement is set to 5 minutes
water_time = datetime.datetime.now()
water = datetime.timedelta(minutes=7)             # Reminder for drinking water is set to 7 minutes


while True:
    real_time = datetime.datetime.now()
    print(real_time.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system('cls')

    if eyes_time + eyes <= real_time:
        play_alarm("eyes.mp3", "Eyes Exercise time!")
        stop_alarm("eydone")
        log("Eyes relaxed")
        eyes_time = datetime.datetime.now()

    if physical_time + physical <= real_time:
        play_alarm("physical.mp3", "Physical Exercise time!")
        stop_alarm("phydone")
        log("Physical fitness")
        physical_time = datetime.datetime.now()

    if water_time + water <= real_time:
        play_alarm("water.mp3", "Water drinking time!")
        stop_alarm("drank")
        log("Drank water")
        water_time = datetime.datetime.now()
