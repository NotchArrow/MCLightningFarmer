import os
import pyautogui
from time import sleep

PATH = os.path.expanduser("~/AppData/Roaming/.minecraft/logs/latest.log")
log_file = open(PATH, "r")
storming = False
singleplayer = True
refresh_interval = 10

while not storming:
	sleep(refresh_interval)
	log_file_lines = log_file.readlines()
	for log_file_line in log_file_lines:
		if "Cat was struck by lightning" in log_file_line:
			storming = True
			break

	if storming:
		if singleplayer:
			pyautogui.press('esc')
			sleep(1)
			for i in range(8):
				pyautogui.press('tab')
				sleep(0.1)
			sleep(1)
			pyautogui.press('\n')
		else:
			pyautogui.typewrite('/stop\n', interval=0.1)
