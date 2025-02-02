import time
from pygame import mixer
from datetime import date, datetime

# Function to play music and wait for a stop command
def play_music(file, stopper, start_time=0):
    mixer.init()
    music = mixer.music
    music.load(file)
    music.play(start=start_time)

    while True:
        stop_command = input(f"Enter '{stopper}' when done >>>>> ")
        if stop_command.lower() == stopper.lower():
            music.stop()
            break

# Function to log messages with timestamp
def log_activity(timestamp, message):
    with open("Record_new_new.txt", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

# Main execution
if __name__ == '__main__':
    # Initialize timers for different activities
    eyes_timer = time.time()
    water_timer = time.time()
    physical_timer = time.time()

    # Time intervals for each activity in seconds
    eyes_interval = 10
    water_interval = 15
    physical_interval = 25

    # Get today's date for the log
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")

    # Write today's date to the log file
    with open("Record_new_new.txt", "a") as file:
        file.write(f"{formatted_date}\n")

    # Define working hours range
    start_time = datetime.strptime("09:00:00", "%H:%M:%S")
    end_time = datetime.strptime("17:00:00", "%H:%M:%S")

    while True:
        # Get the current time and check if it is within the working hours
        current_time_str = time.strftime("%H:%M:%S")
        current_time = datetime.strptime(current_time_str, "%H:%M:%S")

        if current_time < start_time or current_time > end_time:
            print("Outside working hours. Exiting the program.")
            break

        # Check if it's time for eyes workout
        if time.time() - eyes_timer > eyes_interval:
            print("Time for Eyes Workout!")
            play_music('eyes.mp3', "EyDone", 19)
            log_activity(current_time_str, 'Eyes Exercise Done')
            eyes_timer = time.time()

        # Check if it's time to drink water
        elif time.time() - water_timer > water_interval:
            print("Time to drink water!")
            play_music("water.mp3", "Drank", 14)
            log_activity(current_time_str, "Water Drank")
            water_timer = time.time()

        # Check if it's time for physical exercise
        elif time.time() - physical_timer > physical_interval:
            print("Time for physical exercise!")
            play_music("physical.mp3", "ExDone")
            log_activity(current_time_str, "Physical Exercise Done")
            physical_timer = time.time()
