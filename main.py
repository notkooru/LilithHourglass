import time

#Constant variables


#Pomodoro settings
pomodoro_minutes=25
pomodoro_break=5

#System functions
clear=lambda: os.system('cls')
#if UNIX use clear instead of cls

#Database functions


#Pomodoro functions
def clock(minutes):
	time_start=time.perf_counter()
	
	while True:
		time_diff=int(round(time.perf_counter()-time_start))
		time_left=minutes*60-time_diff
		if time_left <= 0:
			print('Pomodoro Finished')
			break

		showTime(time_left)
		time.sleep(1)

def showTime(time_left):
	time_converted=time.strftime("%M:%S", time.gmtime(time_left))
	print(f"Time left: {time_converted}\r", end="\r")

#UI
while True:
	option=input("1. Start pomodoro\n2. Start break\n3. Change pomodoro time\n4. Change pomodoro break time\n")
	
	if option=="1":
		clock(pomodoro_minutes)
	
	elif option=="2":
		clock(pomodoro_break)
	
	elif option=="3":
		pomodoro_new_time=input("Insert your new pomodoro time\n")
		pomodoro_minutes=int(pomodoro_new_time)
		print(f"Your new break time is {pomodoro_minutes}")
	
	elif option=="4":
		pomodoro_new_break=input("Insert your new break time\n")
		pomodoro_break=int(pomodoro_new_break)
		print(f"Your new break time is {pomodoro_break}")
	
	else:
		print(f'"{option}" is not an option')