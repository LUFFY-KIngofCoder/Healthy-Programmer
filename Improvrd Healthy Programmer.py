from pygame import mixer
from datetime import date, datetime
from time import time, strftime

def mujic(file, stopper, start_h=0):
    mixer.init()
    music = mixer.music
    music.load(file)
    music.play(start=start_h)
    while True:
        stop = input(f"Enter {stopper} when done>>>>>>>")
        if stop == stopper:
            music.stop()
            break

def log(tame_n, msg):
    with open("Record new new.txt", "a") as f:
        f.write(f"[{tame_n}] {msg}\n")

if __name__ == '__main__':

    eyes_t = time()
    water_t = time()
    physical_t = time()

    eyesecs = 10  # seconds
    watersecs = 15  # seconds
    physicalsecs = 25  # seconds

    today = date.today()
    d = today.strftime("%B %d, %Y")

    with open("Record new new.txt", "a") as f:
        f.write(f"{d}\n")

    while True:
        tame = strftime("%H:%M:%S")
        current_time = datetime.strptime(tame, "%H:%M:%S")

        # You can set working hours here if needed
        start_time = datetime.strptime("09:00:00", "%H:%M:%S")
        end_time = datetime.strptime("17:00:00", "%H:%M:%S")

        if current_time < start_time or current_time > end_time:
            print("Outside working hours. Exiting program.")
            break

        if time() - eyes_t > eyesecs:
            print("Time For Eyes Workout")
            mujic('eyes.mp3', "EyDone", 19)
            log(tame, 'Eyes Exercise Done')
            eyes_t = time()

        elif time() - water_t > watersecs:
            print("Time to drink water")
            mujic("water.mp3", "Drank", 14)
            log(tame, "Water Drank")
            water_t = time()

        elif time() - physical_t > physicalsecs:
            print("Time to do some physical exercise")
            mujic("physical.mp3", 'ExDone')
            log(tame, "Physical Exercise Done")
            physical_t = time()
