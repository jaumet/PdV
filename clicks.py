__author__ = 'ElectricaProduccions'
import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    #time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    return

click(602, 783) # simulate mouse click at 100px, 100px
time.sleep(0.5)
click(444, 783) # simulate mouse click at 100px, 100px
click(602, 783) # simulate mouse click at 100px, 100px