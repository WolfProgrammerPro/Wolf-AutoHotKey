import pyautogui as pg
import keyboard
import time

key1 = "ctrl+alt+1"
key2 = "ctrl+alt+2"
key3 = "ctrl+alt+3"
key4 = "ctrl+alt+4"
canPressKey = True

while True:
    if  canPressKey:
        if keyboard.is_pressed(key1):
             canPressKey = False
             pg.hotkey("/")
             time.sleep(0.1)
             pg.typewrite("/me ", 0.1)
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(0.1)
             pg.typewrite("bcgjkmpjdfk fgntxre FB-2", 0.01)
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(3)
             canPressKey = True
        elif keyboard.is_pressed(key2):
             canPressKey = False
             pg.hotkey("/")
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(0.1)
             pg.typewrite("Plhfdbz ;tkf.! \"nj j[hfyztvfz nthhbnjhbz! Ljkj;bnt wtkm dbpbnf", 0.01)
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(3)
             canPressKey = True
        elif keyboard.is_pressed(key3):
             canPressKey = False
             pg.hotkey("/")
             time.sleep(0.1)
             pg.typewrite("/me ")
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(0.1)
             pg.typewrite("E,hfk jhe;bt pf cgbye? Cyzk c gjzcf yfhexybrb b yfltk yf xtkjdtrf yfghjnbd", 0.01)
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(3)
             canPressKey = True
        elif keyboard.is_pressed(key4):
             canPressKey = False
             pg.hotkey("/")
             time.sleep(0.1)
             pg.typewrite("/me ")
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(0.1)
             pg.typewrite("Gjcnfdbk jhe;bt yf ghtlj[hfybntkm b e,hfk pf cgbye/ Ljcnfk bp gjlcevrf tle b gthtrecbk/ Dpzk jhe;bt d herb b cyzk c ghtlj[hfybntkz", 0.01)
             time.sleep(0.1)
             pg.hotkey("winleft", "space")
             time.sleep(3)
             canPressKey = True
