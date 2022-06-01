import time
from playsound import playsound
import os


def display(name, minute, second, sche):
    os.system("cls")
    if second >= 10:
        print(name, minute, ':', second, sche, sep='')
    else:
        print(name, minute, ':0', second, sche, sep='')


def timer(name, minute_input, sche):
    minute = minute_input
    sec = 0
    while 60 * minute + sec != 0:
        time.sleep(1)  # when speed up, use 0
        sec = sec - 1
        if sec < 0:
            sec = 59
            minute = minute - 1
        display(name, minute, sec, sche)


min_input = int(input("Please input the duration of every period. (Unit:minute)\nDefault:25\n") or 25)
cyc_input = int(input("Please input the number of periods.\nDefault:3\n") or 3)
rest_input = int(input("Please input the duration of short break. (Unit:minute)\nDefault:10\n") or 10)
long_rest_input = int(input("Please input the duration of long break. (Unit:minute)\nDefault:30\n") or 30)


# main
while True:
    cyc = 0
    while cyc < cyc_input:
        cyc += 1
        timer('Work: ', min_input, ' Now: ' + str(cyc) + '/' + str(cyc_input))
        playsound("C:/Windows/Media/Alarm05.wav")
        timer('Rest: ', rest_input, ' Now: ' + str(cyc) + '/' + str(cyc_input))
        playsound("C:/Windows/Media/Alarm02.wav")
        playsound("C:/Windows/Media/Alarm02.wav")
    timer('Work: ', min_input, ' Now: ' + str(cyc) + '/' + str(cyc_input))
    playsound("C:/Windows/Media/Alarm10.wav")
    timer('Rest: ', long_rest_input, ' Prepare for next period!')
    playsound("C:/Windows/Media/Alarm02.wav")
    playsound("C:/Windows/Media/Alarm02.wav")
