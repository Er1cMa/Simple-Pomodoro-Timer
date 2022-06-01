import time
from playsound import playsound
import os


def display(name, minute, second, sche):
    os.system("cls")
    if second >= 10:
        print(name, minute, ':', second, sche, sep='')
    else:
        print(name, minute, ':0', second, sche, sep='')


def timer(name, min_in, sche):
    min_def = min_in
    sec = 0
    while 60 * min_def + sec != 0:
        time.sleep(1)  # when speed up, use 0
        sec = sec - 1
        if sec < 0:
            sec = 59
            min_def = min_def - 1
        display(name, min_def, sec, sche)


min_input = int(input("Please input the duration of every period. (Unit:minute)\n"))
cyc_input = int(input("Please input the number of periods.\n"))
rest = int(input("Please input the duration of short break. (Unit:minute)\n"))
cyc = cyc_input
while cyc > 1:
    cyc = cyc - 1
    timer('Work: ', min_input, ' Now ' + str(cyc_input-cyc) + '/' + str(cyc))
    playsound("C:/Windows/Media/Alarm05.wav")
    timer('Rest: ', rest, ' Now ' + str(cyc_input-cyc) + '/' + str(cyc))
    playsound("C:/Windows/Media/Alarm02.wav")
    playsound("C:/Windows/Media/Alarm02.wav")
timer('Work: ', min_input, ' Now ' + str(cyc_input-cyc) + '/' + str(cyc))
playsound("C:/Windows/Media/Alarm10.wav")

# Update log:
# Release 1.3.0 08:47 Jun.1
#   Improved display.
# Release 1.2.0 14:54 May.31
#    Added Rest Module.
# Release 1.1.0 14:45 May.31
#    Added Clear-Window Module.
# Release 1.0.0 14:27 May.31
#    Fixed dozens of bugs.

# should add a check input feature!
