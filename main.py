#CountdownTimer

# module
import time

# Function: CountdownTimer
def CountdownTimer():
    timer = int(input("Please enter time in seconds: ")) # time input

    while timer:
        m, s = divmod(timer, 60) # get minutes and seconds of timer
        print(f"{m:02d}:{s:02d}", end="\r") # show timer in two digits format
        time.sleep(1) # freeze 1 second
        timer-=1 # countdown 1 second

    print("Time is up!")

# run function
CountdownTimer()
