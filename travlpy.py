import urllib2 as net
from curses import *
import time
import threading as t


def animation(scr):
    '''for pos in range(dims[1]-12):
        scr.clear()
        scr.addstr(dims[0]/2, pos, "hi")

        scr.refresh()
        time.sleep(0.1)
    '''
    while 1:
        scr.addstr(2, 12, time.strftime("%a, %d %b %Y %H:%M:%S"))
        scr.refresh()
        time.sleep(1)
        scr.clear()

def main():
    scr = initscr()
    noecho()
    curs_set(0)
    scr.keypad(1)
    
    scr.nodelay(1)
    dims = scr.getmaxyx()

    trd = t.Thread(animation(scr))
    trd.daemon = True
    trd.start()

    while 1:
        key = scr.getch()
        if key == ord('q'):
            break

    endwin()

if (__name__ == "__main__"):
    main()

