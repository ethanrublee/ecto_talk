#!/usr/bin/python
import dbus, pprint, sys, tty, termios

session_bus = dbus.SessionBus()
okunames = [n for n in session_bus.list_names() if n.find('okular') != -1]

print "Found okulae:\n\t", "\n\t".join(okunames), "\n"

okula = [session_bus.get_object(n, '/okular') for n in okunames]

def next_slide():
    global okula
    [app.slotNextPage() for app in okula]
    
def prev_slide():
    global okula
    [app.slotPreviousPage() for app in okula]

def quit():
    global old_settings
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)
    print "Exiting"
    sys.exit(0)

dispatch = { ' ' : next_slide,
             'n' : next_slide,
             'b' : prev_slide,
             'p' : prev_slide,
             'q' : quit}
dispatch

pprint.pprint(dispatch)
print '%'*40, "\n"


fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(fd)

while True:
    print "\n\r> ",
    ch = sys.stdin.read(1)
    if ch in dispatch:
        print ch, ord(ch), 
        dispatch[ch]()
    else:
        print ch, "???",
