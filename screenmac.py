from subprocess import call
import time
import sys
num = 1
freq = 2
if(len(sys.argv) == 3):
    dur = int(sys.argv[1])
    freq = int(sys.argv[2])
    num = int((dur * 60) / freq)
if(freq < 1): freq = 1
if(num < 1): num = 1
print("Duration : " + str(dur) + " min\nNumber of screens: " + str(num) + "\nTime freq: " + str(freq) + "\nStarting...")
for count in range(0, num):
    time.sleep(freq)
    name = "slide"
    name = name + str(count)
    name = name + ".jpg" 
    call(["screencapture", name])
    print("Saved screen " + name)