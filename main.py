
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Timer Completed!')

time_input = int(input("Enter the time in seconds: "))

if time_input < 0:
    print("Enter a valid number!")

elif time_input == 0:
    print("You entered zero!")

else:
    countdown(int(time_input))

