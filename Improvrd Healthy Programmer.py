from pygame import mixer
from datetime import date
from time import time,strftime

def mujic(file , stopper, start_h = 0):
    mixer.init()
    music = mixer.music
    music.load(file)
    music.play(start = start_h)
    while True:
        stop = input(f"Enter {stopper} when done>>>>>>>")
        if stop == stopper:
            music.stop()
            break

def log(tame_n, msg):
    with open("Record new new.txt" , "a") as f:
        f.write("[tame_n] {msg}\n")
if __name__ == '__main__':

    eyes_t = time()
    water_t = time()
    physical_t = time()

    eyesecs = 10
    watersecs = 15
    physicalsecs = 25

    # tame = strftime("%H:%M:%S")
    #
    # while tame >= '17:00:00' and tame <= '09:00:00':
    #     tame = strftime("%H:%M:%S")
    #
    today = date.today()

    d = today.strftime("%B %d, %Y")

    with open("Record new new.txt", "a") as f:
        f.write(f"{d}\n")

    # while tame >= '09:00:00' and tame <= '17:00:00':
    while True:
        tame = strftime("%H:%M:%S")

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
