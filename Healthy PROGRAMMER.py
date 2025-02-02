from datetime import date
import time
from pygame import mixer


def mujic(file , start1, stopper):
    music = mixer.music
    mixer.init()
    music.load(file)
    music.play(start = start1)
    while True:
        stop = input(f'Type \"{stopper}\" when completed the task')
        if stop == stopper:
            music.stop()
            break
def log(msg , tame_n):
    with open("Record.txt" , "a") as f:
        f.write(f"[{tame_n}] {msg}\n")


def eye():
    tame_n = time.strftime("%H:%M:%S")
    mujic('eyes.mp3' , 19, "EyDone" )
    f.write(f"[{tame_n}] Eyes Exercise Done\n")


def physical():
    tame_n = time.strftime("%H:%M:%S")
    mujic('physical.mp3' , 0, "ExDone" )
    f.write(f"[{tame_n}]  Done\n")

def water():
    tame_n = time.strftime("%H:%M:%S")
    mujic('water.mp3' , 14, "Drank" )
    f.write(f"[{tame_n}] Drank Water\n")

if __name__ == '__main__':
    tame = time.strftime("%H:%M:%S")
    today = date.today()
    d = today.strftime("%B %d, %Y")

    f = open('Record.txt' , 'a')
    f.write(f"{d}\n")

    while tame >= '17:00:00' and tame <= '09:00:00':
        tame = time.strftime("%H:%M:%S")

    t1 = time.time()
    time.sleep(5)
    
    while tame >= '09:00:00' and tame <= '17:00:00':
        tame = time.strftime("%H:%M:%S")
        t2 = time.time()
        diff = round(t2 - t1) / 60

        if diff % 45 == 0 and diff % 30 == 0:
            eye()
            time.sleep(2)
            physical()

        elif diff % 35 == 0 and diff % 30 == 0:
            water()
            time.sleep(2)
            eye()

        elif diff % 35 == 0 and diff % 45 == 0:
            physical()
            time.sleep(2)
            water()

        elif diff % 35 == 0:
            water()

        elif diff % 30 == 0:
            eye()

        elif diff % 45 == 0:
            physical()

    f.close()