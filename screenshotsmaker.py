import gi
import time
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk
# screenshot active window
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
	screen = Gdk.get_default_root_window().get_screen()
	w = screen.get_active_window()
	print(w)
	pb = Gdk.pixbuf_get_from_window(w, 1, 1, 100, 100)
	name = "slide"
	name = name + str(count)
	name = name + ".png" 
	pb.savev(name, "png", (), ())
	print("Saved screen " + name)
