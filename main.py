import time
import os
from playsound import playsound
import tkinter
import threading

#Constant variables
height = 400
width = 400

#Pomodoro settings
pomodoro_minutes=0.01
pomodoro_break=0.05
pomodoro_break_long=0.1
pomodoro_count=0
isBreak=False
pomo_or_break="pomodoro"

#System functions
def play(sound):
	soundFilePath=''
	
	if sound=="pomodoro":
		soundFilePath="sounds/finish.wav" #pomodoro sound
	elif sound=="break":
		soundFilePath="sounds/bfinish.wav" #break sound
	elif sound=="pStart":
		soundFilePath="sounds/start.wav" #pomodoro start sound
	elif sound=="bStart":
		soundFilePath="sounds/bstart.wav" #break start sound
	
	playsound(soundFilePath, False)

clear=lambda: os.system('cls')
#if UNIX use clear instead of cls

#Pomodoro functions
def clock():
	global isBreak
	global pomodoro_count
	minutes = 0
	
	if isBreak:
		if pomodoro_count == 4:
			minutes=pomodoro_break_long
		else:
			minutes=pomodoro_break	
		play("bStart")
	else:
		minutes=pomodoro_minutes
		play("pStart")

	time_start=time.perf_counter()
	
	while True:
		time_diff=int(round(time.perf_counter()-time_start))
		time_left=minutes*60-time_diff
		if time_left <= 0:
			print('')
			break

		showTime(time_left)
		time.sleep(1)
	
	if isBreak:
		play("break")
		if pomodoro_count==4:
			pomodoro_count=0
			print("You've finished your long break!")
		else:
			pomodoro_count+=1
			print("You've finished your break!")
		isBreak=False
	else:
		play("pomodoro")
		print("You've finished your pomodoro!")
		isBreak=True
	
	global btnStart
	global lblCurrentState
	btnStart["state"] = "active"
	lblCurrentState.config(text=f"Currently on a break? {isBreak}")

def showTime(time_left):
	global lblTimeLeft
	time_left-=1
	time_converted=time.strftime("%M:%S", time.gmtime(time_left))
	lblTimeLeft.config(text=f"Time left: {time_converted}\r")

def startClockThread():
	threading.Thread(target=clock).start()
	global btnStart
	btnStart["state"] = "disabled"

#Program start functions
clear() #To have a clean console at the start

#GUI
window = tkinter.Tk()

#Window Settings
window.geometry(f"{width}x{height}")
window.maxsize(width, height)
window.minsize(width, height)

#GUI Widgets
#Widget Creation
#Label
lblCurrentState = tkinter.Label(window, text=f"Currently on a break? {isBreak}")
lblTimeLeft = tkinter.Label(window, text="Time left: 00:00")

#Button
btnStart = tkinter.Button(window, text="Start", command=startClockThread)

#Widget Placement
#Label
lblCurrentState.grid(row=0, column=0)
lblTimeLeft.grid(row=2, column=0)

#Button
btnStart.grid(row=1, column=0)


window.mainloop()