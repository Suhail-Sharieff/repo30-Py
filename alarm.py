import time
import datetime
import pygame


soundFile="mixkit-alert-alarm-1005.wav"
while True:
    set_alarm=input(f"Hi...Cuurent time is {(datetime.datetime.now().strftime("%H:%M:%S"))} , so when do u want me to wake u up ? (enter in format (HH:MM:SS))")
    if set_alarm<=(datetime.datetime.now().strftime("%H:%M:%S")):
        print("pls enter valid time...")
    else:
        break
while True:
    currTime=(datetime.datetime.now().strftime("%H:%M:%S"))
    print(f"current time is : {currTime}")
    if set_alarm==currTime:
        print("Wake Up...")

        pygame.mixer.init()
        pygame.mixer.music.load(soundFile)
        pygame.mixer.music.play()

        # to ensure the song is played fully
        while pygame.mixer.music.get_busy():
            time.sleep(1)

        break
    time.sleep(1)